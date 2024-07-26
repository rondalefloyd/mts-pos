import os, sys
from peewee import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import User
from app.utils.database import postgres_db

class Authenticate(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function, entry=None):
        super().__init__()
        self.function = function
        self.entry = entry
        pass
    
    def authenticateUserByPassword(self):
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
                'activeStatus': None,
                'lastLoginTs': None,
                'lastLogoutTs': None,
                'updateTs': None,
            },
        }
        
        try:
            user = User.get(
                (User.UserName == self.entry['userName']) &
                (User.AccessCode == self.entry['accessCode'])
            )
            
            result = {
                'success': True,
                'message': 'Authentication successful.',
                'data': {
                    'id': user.Id,
                    'organizationId': user.OrganizationId,
                    'userName': user.UserName,
                    'accessCode': user.AccessCode,
                    'fullName': user.FullName,
                    'birthDate': user.BirthDate,
                    'mobileNumber': user.MobileNumber,
                    'accessLevel': user.AccessLevel,
                    'activeStatus': user.ActiveStatus,
                    'lastLoginTs': user.LastLoginTs,
                    'lastLogoutTs': user.LastLogoutTs,
                    'updateTs': user.UpdateTs,
                }
            }
            
            return result
        
        except User.DoesNotExist:
            result['message'] = 'Authentication failed. User not found.'
            
            return result

    def run(self):
        postgres_db.connect()

        match self.function:
            case 'pos/authenticate/user/password':
                result = self.authenticateUserByPassword()
            case _:
                result = None

        self.finished.emit(result)
        postgres_db.close()
        pass
