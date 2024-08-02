import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import Users, Organizations, UserSessionInfos
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
            'message': 'N/A',
            'data': [],
        }
        
        try:
            with postgres_db:
                if self.function_route == 'authenticate_user_by_user_name_access_code':
                    message = authenticate_user_by_user_name_access_code(self.entry)
                elif self.function_route == 'unauthenticate_users_by_id':
                    message = unauthenticate_users_by_id(self.entry)
                else:
                    message = "INSERT MESSAGE HERE"
                        
            result['message'] = message
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
        logging.info('result', json.dumps(result, indent=4))
        
# add function here
def authenticate_user_by_user_name_access_code(entry=object):
    pass
def unauthenticate_users_by_id(entry=object):
    pass