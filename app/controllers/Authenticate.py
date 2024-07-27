import os, sys
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import Users, UserSessionInfos
from app.utils.database import postgres_db

class AuthenticateThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function, entry=None):
        super().__init__()
        self.function = function
        self.entry = entry
        pass
    
    def run(self):
        postgres_db.connect()

        match self.function:
            case 'pos/authenticate/user/username/accesscode':
                result = authenticate_user_by_username_accesscode(self.entry)
            case 'pos/unauthenticate/user/id':
                result = unauthenticate_user_by_id(self.entry)
            case _:
                result = None

        self.finished.emit(result)
        postgres_db.close()
        pass

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