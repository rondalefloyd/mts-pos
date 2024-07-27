import os, sys
from peewee import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import Users, Organizations
from app.utils.database import postgres_db

class FetchThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function, entry=None):
        super().__init__()
        self.function = function
        self.entry = entry
    
    def run(self):
        postgres_db.connect()

        match self.function:
            case 'pos/fetch/user/all':
                result = fetch_user()
            case 'pos/fetch/organization/all':
                result = fetch_organization()
            case _:
                result = None

        self.finished.emit(result)
        postgres_db.close()

def fetch_user():
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': []
    }
    
    try:
        users = Users.select().order_by(Users.UpdateTs.desc())
        
        for user in users:
            result['success'] = True
            result['message'] = 'Fetch successful.'
            result['data'].append({
                'id': user.Id,
                'organizationId': user.OrganizationId,
                'userName': user.UserName,
                'accessCode': user.AccessCode,
                'fullName': user.FullName,
                'birthDate': user.BirthDate,
                'mobileNumber': user.MobileNumber,
                'accessLevel': user.AccessLevel,
                'updateTs': user.UpdateTs,
            })
        
    except Users.DoesNotExist:
        result['message'] = 'Fetch failed. Users not found.'
        
    return result

def fetch_organization():
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': []
    }
    
    try:
        organizations = Organizations.select().order_by(Organizations.UpdateTs.desc())
        
        for organization in organizations:
            result['success'] = True
            result['message'] = 'Fetch successful.'
            result['data'].append({
                'id': organization.Id,
                'taxId': organization.TaxId,
                'organizationName': organization.OrganizationName,
                'address': organization.Address,
                'mobileNumber': organization.MobileNumber,
                'accessCode': organization.AccessCode,
                'updateTs': organization.UpdateTs,
            })
        
    except Organizations.DoesNotExist:
        result['message'] = 'Fetch failed. Organizations not found.'
        
    return result
