import os
import sys
from peewee import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import User, Organization
from app.utils.database import postgres_db

class RegisterThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function, entry=None):
        super().__init__()
        self.function = function
        self.entry = entry
    
    def run(self):
        postgres_db.connect()

        match self.function:
            case 'pos/register/user':
                result = registerUser(self.entry)
            case 'pos/register/organization':
                result = registerOrganization(self.entry)
            case _:
                result = None

        self.finished.emit(result)
        postgres_db.close()

def registerUser(entry):
    result = {
        'success': False,
        'message': 'Registration failed.',
    }
    
    try:
        user = User.get(User.UserName == entry['userName'])
        
        if user.UserName == entry['userName']:
            result['message'] = 'User already exists with the given username.'
        
        return result
    
    except User.DoesNotExist:
        user = User.create(
            OrganizationId=Organization.get(Organization.OrganizationName == entry['organizationName']).Id,
            UserName=entry['userName'],
            AccessCode=entry['accessCode'],
            FullName=entry['fullName'],
            BirthDate=entry['birthDate'],
            MobileNumber=entry['mobileNumber'],
            AccessLevel=entry['accessLevel']
        )
        
        result = {
            'success': True,
            'message': 'User registered successfully.',
        }
        
        return result

def registerOrganization(entry):
    result = {
        'success': False,
        'message': 'Organization registration failed.',
    }
    
    try:
        organization = Organization.get(Organization.TaxId == entry['taxId'])
        
        if organization.TaxId == entry['taxId']:
            result['message'] = 'Organization already exists with the given Tax ID.'
        
        return result
    
    except Organization.DoesNotExist:
        organization = Organization.create(
            TaxId=entry['taxId'],
            OrganizationName=entry['organizationName'],
            Address=entry['address'],
            MobileNumber=entry['mobileNumber'],
            AccessCode=entry['accessCode']
        )
        
        result = {
            'success': True,
            'message': 'Organization registered successfully.',
        }
        
        return result
