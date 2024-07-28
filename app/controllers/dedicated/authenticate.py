import os, sys, logging
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import Users, Organizations, UserSessionInfos
from app.controllers.common.validator import entry_has_value
from app.controllers.common.messages import (
    exception_error_message,
    integrity_error_message,
    function_route_not_exist,
)
from app.utils.database import postgres_db

logging.basicConfig(level=logging.INFO)

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
            'data': [],
        }
        try:
            with postgres_db:
                match self.function_route:
                    case 'pos/authenticate/user/username/accesscode':
                        result = authenticate_user_by_username_accesscode(self.entry)
                    case 'pos/unauthenticate/user/id':
                        result = unauthenticate_user_by_id(self.entry)
                    case _:
                        result['message'] = function_route_not_exist(self.function_route, self.__class__.__name__)

            self.finished.emit(result)
            
        except Exception as error:
            result['message'] = exception_error_message(error)
            postgres_db.rollback()
            self.finished.emit(result)
            logging.error('error: ', error)
            logging.info('database rolled back...')
            
        finally:
            postgres_db.close()
            logging.info('database closed...')

def authenticate_user_by_username_accesscode(entry):
    result = {
        'success': False,
        'message': 'Authenticate failed.',
        'data': {
            'id': None,
            'organizationId': None,
            'organizationName': None,
            'userName': None,
            'accessCode': None,
            'fullName': None,
            'birthDate': None,
            'mobileNumber': None,
            'accessLevel': None,
            'updateTs': None,
        },
    }
    
    if entry_has_value(alpha_entry=['userName', 'accessCode'], entry=entry) is False:
        result['message'] = 'Invalid entry.'
        return result
    
    try:
        users = Users.select().where(
            (Users.UserName == entry['userName']) &
            (Users.AccessCode == entry['accessCode'])
        )
        if not users.exists():
            result['message'] = 'Authenticate failed. User not found.'
            return result
        
        users = users.first()
        
        userSessionInfos = UserSessionInfos.select().where(UserSessionInfos.UserId == users.Id)        
        if not userSessionInfos.exists():
            result['message'] = 'User session information not found.'
            return result
        
        userSessionInfos = userSessionInfos.first()
        userSessionInfos.ActiveStatus = 1
        userSessionInfos.LastLoginTs = datetime.now()
        userSessionInfos.save()
        
        result['success'] = True
        result['message'] = 'Authenticate successful.'
        result['data'] = {
            'id': users.Id,
            'organizationId': users.OrganizationId,
            'organizationName': Organizations.select(Organizations.OrganizationName).where(Organizations.Id == users.OrganizationId).first(),
            'userName': users.UserName,
            'accessCode': users.AccessCode,
            'fullName': users.FullName,
            'birthDate': users.BirthDate,
            'mobileNumber': users.MobileNumber,
            'accessLevel': users.AccessLevel,
            'updateTs': users.UpdateTs,
        }
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def unauthenticate_user_by_id(entry):
    result = {
        'success': False,
        'message': 'Unauthentication failed.',
    }
    
    try:
        userSessionInfos = UserSessionInfos.select().where(UserSessionInfos.UserId == entry['userId'])        
        if not userSessionInfos.exists():
            result['message'] = 'User session information not found.'
            return result
        
        userSessionInfos = userSessionInfos.first()
        userSessionInfos.ActiveStatus = 0
        userSessionInfos.LastLogoutTs = datetime.now()
        userSessionInfos.save()
        
        result['success'] = True
        result['message'] = 'Unauthentication successful.'
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result