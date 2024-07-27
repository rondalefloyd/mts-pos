import os, sys
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import Users, UserSessionInfos, Organizations
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
                result = register_user(self.entry)
            case 'pos/register/organization':
                result = register_organization(self.entry)
            case _:
                result = None

        self.finished.emit(result)
        postgres_db.close()

def register_user(entry):
    result = {
        'success': False,
        'message': 'Registration failed.',
    }
    
    try:
        users = Users.get(Users.UserName == entry['userName'])
        
        if users.UserName == entry['userName']:
            result['message'] = 'User already exists with the given username.'
        
    except Users.DoesNotExist:
        users = Users.create(
            OrganizationId=Organizations.get(Organizations.OrganizationName == entry['organizationName']).Id,
            UserName=entry['userName'],
            AccessCode=entry['accessCode'],
            FullName=entry['fullName'],
            BirthDate=entry['birthDate'],
            MobileNumber=entry['mobileNumber'],
            AccessLevel=entry['accessLevel']
        )
        
        UserSessionInfos.create(
            UserId=users.Id,
            ActiveStatus=1,
            LastLoginTs=datetime.now(),
            UpdateTs=datetime.now()
        )
        
        result['success'] = True
        result['message'] = 'User registered successfully.'
        
    return result

def register_organization(entry):
    result = {
        'success': False,
        'message': 'Organization registration failed.',
    }
    
    try:
        organizations = Organizations.get(Organizations.TaxId == entry['taxId'])
        
        if organizations.TaxId == entry['taxId']:
            result['message'] = 'Organization already exists with the given Tax ID.'
        
    except Organizations.DoesNotExist:
        organizations = Organizations.create(
            TaxId=entry['taxId'],
            OrganizationName=entry['organizationName'],
            Address=entry['address'],
            MobileNumber=entry['mobileNumber'],
            AccessCode=entry['accessCode']
        )
        
        result['success'] = True
        result['message'] = 'Organization registered successfully.'
        
    return result
