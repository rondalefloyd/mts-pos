import os
import sys
from peewee import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import User, Organization
from app.utils.database import postgres_db

class Register(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function, entry=None):
        super().__init__()
        self.function = function
        self.entry = entry
    
    def registerUser(self):
        result = {
            'success': False,
            'message': 'Registration failed.',
        }
        
        try:
            user = User.get((User.userName == self.entry['userName']))
            
            if user.userName == self.entry['userName']:
                result['message'] = 'User already exists with the given username.'
            
            return result
        
        except User.DoesNotExist:
            user = User.create(
                organizationId=self.entry['organizationId'],
                userName=self.entry['userName'],
                accessCode=self.entry['accessCode'],
                fullName=self.entry['fullName'],
                birthDate=self.entry['birthDate'],
                mobileNumber=self.entry['mobileNumber'],
                accessLevel=self.entry['accessLevel']
            )
            
            result = {
                'success': True,
                'message': 'User registered successfully.',
            }
            
            return result

    def registerOrganization(self):
        result = {
            'success': False,
            'message': 'Organization registration failed.',
        }
        
        try:
            organization = Organization.get((Organization.taxId == self.entry['taxId']))
            
            if organization.taxId == self.entry['taxId']:
                result['message'] = 'Organization already exists with the given Tax ID.'
            
            return result
        
        except Organization.DoesNotExist:
            organization = Organization.create(
                taxId=self.entry['taxId'],
                organizationName=self.entry['organizationName'],
                address=self.entry['address'],
                mobileNumber=self.entry['mobileNumber'],
                accessCode=self.entry['accessCode']
            )
            
            result = {
                'success': True,
                'message': 'Organization registered successfully.',
            }
            
            return result

    def run(self):
        postgres_db.connect()

        match self.function:
            case 'pos/register/user':
                result = self.registerUser()
            case 'pos/register/organization':
                result = self.registerOrganization()
            case _:
                result = None

        self.finished.emit(result)
        postgres_db.close()
