import os, sys
from peewee import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.model_association import User
from app.utils.database import postgres_db

class Register(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function, entry=None):
        super().__init__()
        self.function = function
        self.entry = entry
        pass
    
    def register_user(self):
        result = {
            'success': False,
            'message': 'Registration failed.',
        }
        
        try:
            user = User.get((User.UserName == self.entry['userName']))
            
            if user.UserName == self.entry['userName']:
                result['message'] = 'User already exists with the given username.'
            
            return result
        
        except User.DoesNotExist:
            user = User.create(
                OrganizationId=self.entry['organizationId'],
                UserName=self.entry['userName'],
                AccessCode=self.entry['accessCode'],
                FullName=self.entry['fullName'],
                BirthDate=self.entry['birthDate'],
                MobileNumber=self.entry['mobileNumber'],
                AccessLevel=self.entry['accessLevel']
            )
            
            result = {
                'success': True,
                'message': 'User registered successfully.',
            }
            
            return result

    def run(self):
        postgres_db.connect()

        match self.function:
            case 'pos/register/user':
                result = self.register_user()
            case _:
                result = None

        self.finished.emit(result)
        postgres_db.close()
        pass
