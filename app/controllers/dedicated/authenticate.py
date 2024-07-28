import os, sys, logging
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import Users, UserSessionInfos
from app.controllers.common.messages import (
    class_error_message, 
    function_route_error_message,
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
            'message': class_error_message(self.__class__.__name__),
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
            result['message'] = function_route_error_message(self.function_route, error)
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
        'message': 'Authentication failed.',
        'data': {
            'id': None,
            'organizationId': None,
            'userName': None,
            'accessCode': None,
            'fullName': None,
            'birthDate': None,
            'mobileNumber': None,
            'accessLevel': None,
            'updateTs': None,
        },
    }
    
    try:
        users = Users.get(
            (Users.UserName == entry['userName']) &
            (Users.AccessCode == entry['accessCode'])
        )
        
        userSessionInfos = UserSessionInfos.get(UserSessionInfos.UserId == users.Id)
        userSessionInfos.ActiveStatus = 1
        userSessionInfos.LastLoginTs = datetime.now()
        userSessionInfos.save()
        
        result['success'] = True
        result['message'] = 'Authentication successful.'
        result['data'] = {
            'id': users.Id,
            'organizationId': users.OrganizationId,
            'userName': users.UserName,
            'accessCode': users.AccessCode,
            'fullName': users.FullName,
            'birthDate': users.BirthDate,
            'mobileNumber': users.MobileNumber,
            'accessLevel': users.AccessLevel,
            'updateTs': users.UpdateTs,
        }
        
    except Users.DoesNotExist:
        result['success'] = False
        result['message'] = 'Authentication failed. User not found.'
        
    return result

def unauthenticate_user_by_id(entry):
    result = {
        'success': False,
        'message': 'Unauthentication failed.',
    }
    
    try:
        userSessionInfos = UserSessionInfos.get(UserSessionInfos.UserId == entry['userId'])
        
        userSessionInfos.ActiveStatus = 0
        userSessionInfos.LastLogoutTs = datetime.now()
        userSessionInfos.save()
        
        result['success'] = True
        result['message'] = 'Unauthentication successful.'
        
    except UserSessionInfos.DoesNotExist:
        result['message'] = 'Authentication failed. User not found.'
        
    return result