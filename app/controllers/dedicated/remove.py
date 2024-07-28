import os, sys, logging
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import (
    Users,
    UserSessionInfos,
    Members,
    Promos,
    Rewards,
)
from app.controllers.common.messages import (
    exception_error_message,
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
            'message': 'N/A',
        }
        try:
            with postgres_db:
                match self.function_route:
                    case 'pos/remove/user/id':
                        result = remove_user_by_id(self.entry)
                    case 'pos/remove/member/id':
                        result = remove_member_by_id(self.entry)
                    case 'pos/remove/promo/id':
                        result = remove_promo_by_id(self.entry)
                    case 'pos/remove/reward/id':
                        result = remove_reward_by_id(self.entry)
                    case _:
                        result['message'] = function_route_not_exist(self.function_route, self.__class__.__name__)


            self.finished.emit(result)
            
        except Exception as error:
            result['message'] = exception_error_message(error)
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
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def remove_member_by_id(entry):
    result = {
        'success': False,
        'message': 'Remove failed.',
    }
    
    try:
        members = Members.delete().where(Members.Id == entry['id'])
        members.execute()
        
        result['success'] = True
        result['message'] = 'Remove successful.'
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def remove_promo_by_id(entry):
    result = {
        'success': False,
        'message': 'Remove failed.',
    }
    
    try:
        promos = Promos.delete().where(Promos.Id == entry['id'])
        promos.execute()
        
        result['success'] = True
        result['message'] = 'Remove successful.'
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def remove_reward_by_id(entry):
    result = {
        'success': False,
        'message': 'Remove failed.',
    }
    
    try:
        rewards = Rewards.delete().where(Rewards.Id == entry['id'])
        rewards.execute()
        
        result['success'] = True
        result['message'] = 'Remove successful.'
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result