import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import Users, Organizations, UserSessionInfos
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
                elif self.function_route == 'unauthenticate_users_by_id':
                    result = unauthenticate_users_by_id(self.entry, result)
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
        print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))
        
# add function here
def authenticate_user_by_user_name_access_code(entry=None, result=None):
    try:
        user = Users.select().where(
            (Users.UserName == entry['userName']) & 
            (Users.AccessCode == entry['accessCode'])
        )
        if not user.exists():
            result['message'] = 'User does not exists'
            return result
        user = user.first()
        
        userSessionInfos = UserSessionInfos.select().where(UserSessionInfos.Id == user.Id)
        if not userSessionInfos.exists():
            result['message'] = 'UserSession does not exists'
            return result
        userSessionInfos = userSessionInfos.first()
        userSessionInfos.ActiveStatus = 1
        userSessionInfos.LastLoginTs = datetime.now()
        userSessionInfos.save()
        
        result['success'] = True
        result['dictData'] = {
            'userId': user.id,
            'organizationName': Organizations.get_or_none(Organizations.Id == user.OrganizationId).OrganizationName,
            'userName': user.UserName,
            'accessCode': user.AccessCode,
            'fullName': user.FullName,
            'birthDate': user.BirthDate,
            'mobileNumber': user.MobileNumber,
            'accessLevel': user.AccessLevel,
        }
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result

def unauthenticate_users_by_id(entry=None, result=None):
    try:
        userSessionInfos = UserSessionInfos.select().where(UserSessionInfos.Id == entry['id'])
        
        if not userSessionInfos.exists():
            result['message'] = 'UserSession does not exists'
            return result
        
        userSessionInfos = userSessionInfos.first()
        userSessionInfos.ActiveStatus = 0
        userSessionInfos.save()
        
        result['success'] = True
        
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result