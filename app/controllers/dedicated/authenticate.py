import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import Users, Organizations, UserSessionInfos
from app.utils.databases import postgres_db

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
            'oneData': {},
            'manyData': [],
        }
        
        try:
            with postgres_db:
                if self.function_route == 'authenticate_user_by_user_name_access_code':
                    result = authenticate_user_by_user_name_access_code(self.entry, result)
                elif self.function_route == 'unauthenticate_users_by_id':
                    result = unauthenticate_users_by_id(self.entry, result)
                else:
                    result['message'] = f"'{self.function_route}' is an invalid function..."
                        
            logging.info('database operation done...')
            
        except Exception as exception:
            result['message'] = exception
            postgres_db.rollback()
            logging.error('exception: ', exception)
            logging.info('database operation rolled back...')
            
        finally:
            postgres_db.close()
            logging.info('database closed...')
            
        self.finished.emit(result)
        print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))
        
# add function here
def authenticate_user_by_user_name_access_code(entry=None, result=None):
    try:
        users = Users.select().where(
            (Users.UserName == entry['userName']) & 
            (Users.AccessCode == entry['accessCode'])
        )
        
        if not users.exists():
            result['message'] = 'User does not exists'
            return result
        
        users = users.first()
        
        result['success'] = True
        result['oneData'] = {
            'organizationName': Organizations.get(Organizations.Id == users.OrganizationId).OrganizationName,
            'userName': users.UserName,
            'accessCode': users.AccessCode,
            'fullName': users.FullName,
            'birthDate': users.BirthDate,
            'mobileNumber': users.MobileNumber,
            'accessLevel': users.AccessLevel,
        }
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result

def unauthenticate_users_by_id(entry=object):
    pass