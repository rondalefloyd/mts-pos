import os, sys, logging
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import Users, UserSessionInfos, Organizations
from app.controllers.common.messages import (
    class_error_message, 
    function_route_error_message,
    function_route_not_exist,
)
from app.utils.database import postgres_db

logging.basicConfig(level=logging.INFO)

class RegisterThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function_route, entry=None):
        super().__init__()
        self.function_route = function_route
        self.entry = entry
    
    def run(self):
        result = {
            'success': False,
            'message': class_error_message(self.__class__.__name__),
        }
        try:
            with postgres_db:
                match self.function_route:
                    case 'pos/register/user':
                        result = register_user(self.entry)
                    case 'pos/register/organization':
                        result = register_organization(self.entry)
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
        try:
            users = Users.create(
                OrganizationId=f"{Organizations.get(Organizations.OrganizationName == entry['organizationName']).Id}",
                UserName=entry['userName'],
                AccessCode=entry['accessCode'],
                FullName=entry['fullName'],
                BirthDate=entry['birthDate'],
                MobileNumber=entry['mobileNumber'],
                AccessLevel=entry['accessLevel']
            )
            
            UserSessionInfos.create(
                UserId=users.Id,
                ActiveStatus=0,
            )
            
            result['success'] = True
            result['message'] = 'User registered successfully.'
            
        except Organizations.DoesNotExist:
            result['message'] = 'Organization does not exists.'
        
        
        
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
