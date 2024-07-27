import os, sys
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import Users, UserSessionInfos
from app.utils.database import postgres_db

class RemoveThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function, entry=None):
        super().__init__()
        self.function = function
        self.entry = entry
    
    def run(self):
        try:
            postgres_db.connect()

            match self.function:
                case 'pos/remove/user/id':
                    result = remove_user_by_id(self.entry)
                case _:
                    result = None

            self.finished.emit(result)
            
        except Exception as error:
            postgres_db.rollback()
            print('error: ', error)
            print('database rolled back...')
            
        finally:
            postgres_db.close()
            print('database closed...')

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

