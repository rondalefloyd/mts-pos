import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import User, Organization, UserSession
from app.utils.databases import postgres_db


class AuthenticateThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function_route, entry=None):
        super().__init__()
        self.function_route = function_route
        self.entry = entry
    
    def run(self):
        result = {
            'success': False,
            'message': 'N/A',
            'dictData': {},
            'listData': [],
        }
        
        try:
            with postgres_db:
                if self.function_route == 'authenticate_user_by_user_name_access_code':
                    result = authenticate_user_by_user_name_access_code(self.entry, result)
                elif self.function_route == 'unauthenticate_user_by_id':
                    result = unauthenticate_user_by_id(self.entry, result)
                else:
                    result['message'] = f"'{self.function_route}' is an invalid function..."
                        
            logging.info('database operation done...')
            
        except Exception as exception:
            result['message'] = exception
            postgres_db.rollback()
            logging.error('exception: ', exception)
            logging.info('database operation rolled back...')
            
        finally:
            postgres_db.close()
            logging.info('database closed...')
            
        self.finished.emit(result)
        # print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))
        
def authenticate_user_by_user_name_access_code(entry=None, result=None):
    try:
        user = User.select().where(
            (User.UserName == entry['userName']) & 
            (User.AccessCode == entry['accessCode'])
        )
        if not user.exists():
            result['message'] = 'User does not exists'
            return result
        user = user.first()
        
        organization = Organization.select().where(Organization.Id == user.OrganizationId)
        if not organization.exists():
            result['message'] = 'Organization in this user does not exists'
            return result
        organization = organization.first()
        
        userSessions = UserSession.select().where(UserSession.Id == user.Id)
        if not userSessions.exists():
            result['message'] = 'UserSession does not exists'
            return result
        userSessions = userSessions.first()
        userSessions.ActiveStatus = 1
        userSessions.LastLoginTs = datetime.now()
        userSessions.save()
        
        organization = user.OrganizationId
        
        result['success'] = True
        result['dictData'] = {
            'user': {
                'id': user.Id,
                'organizationId': user.OrganizationId,
                'userName': user.UserName,
                'accessCode': user.AccessCode,
                'fullName': user.FullName,
                'birthDate': user.BirthDate,
                'mobileNumber': user.MobileNumber,
                'accessLevel': user.AccessLevel,
            },
            'organization': {
                'id': organization.Id,
                'taxId': organization.TaxId,
                'organizationName': organization.OrganizationName,
                'address': organization.Address,
                'mobileNumber': organization.MobileNumber,
                'accessCode': organization.AccessCode,
            }
        }
        
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result

def unauthenticate_user_by_id(entry=None, result=None):
    try:
        userSession = UserSession.select().where(UserSession.UserId == entry['id'])
        
        if not userSession.exists():
            result['message'] = 'UserSession does not exists'
            return result
        
        userSession = userSession.first()
        userSession.ActiveStatus = 0
        userSession.save()
        
        result['success'] = True
        
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result