import os, sys, logging
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import Users, UserSessionInfos
from app.controllers.common.messages import (
    class_error_message, 
    function_route_error_message,
    function_route_not_exist,
)
from app.utils.database import postgres_db

class RemoveThread(QThread):
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
                    case 'pos/remove/user/id':
                        result = remove_user_by_id(self.entry)
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

def remove_user_by_id(entry):
    result = {
        'success': False,
        'message': 'Remove failed.',
    }
    
    try:
        users = Users.delete().where(Users.Id == entry['id'])
        users.execute()
        
        userSessionInfos = UserSessionInfos.delete().where(UserSessionInfos.UserId == entry['id'])
        userSessionInfos.execute()
        
        result['success'] = True
        result['message'] = 'Remove successful.'
        
    except Users.DoesNotExist:
        result['success'] = False
        result['message'] = 'Remove failed. User not found.'
        
    return result

