import os, sys, logging, math, json
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
    ItemPrices,
)
from app.utils.databases import postgres_db

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
            'dictData': {},
            'listData': [],
        }
        
        try:
            with postgres_db:
                if self.function_route == 'remove_item_prices_by_id':
                    result = remove_item_prices_by_id(self.entry, result)
                elif self.function_route == 'remove_members_by_id':
                    result = remove_members_by_id(self.entry, result)
                elif self.function_route == 'remove_promos_by_id':
                    result = remove_promos_by_id(self.entry, result)
                elif self.function_route == 'remove_rewards_by_id':
                    result = remove_rewards_by_id(self.entry, result)
                elif self.function_route == 'remove_users_by_id':
                    result = remove_users_by_id(self.entry, result)
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
def remove_item_prices_by_id(entry=None, result=None):
    # TODO: finish this
    return result
    pass
def remove_members_by_id(entry=None, result=None):
    try:
        member = Members.select().where(Members.Id == entry['id'])
        
        if not member.exists():
            result['message'] = 'Member does not exists'
            return
        
        member.get_or_none().delete_instance()
        
        result['success'] = True
        result['message'] = 'Member deleted'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def remove_promos_by_id(entry=None, result=None):
    try:
        promo = Promos.select().where(Promos.Id == entry['id'])
        
        if not promo.exists():
            result['message'] = 'Promo does not exists'
            return
        
        promo.get_or_none().delete_instance()
        
        result['success'] = True
        result['message'] = 'Promo deleted'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def remove_rewards_by_id(entry=None, result=None):
    try:
        reward = Rewards.select().where(Rewards.Id == entry['id'])
        
        if not reward.exists():
            result['message'] = 'Reward does not exists'
            return
        
        reward.get_or_none().delete_instance()
        
        result['success'] = True
        result['message'] = 'Reward deleted'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def remove_users_by_id(entry=None, result=None):
    try:
        user = Users.select().where(Users.Id == entry['id'])
        
        if not user.exists():
            result['message'] = 'User does not exists'
            return
        
        user.get_or_none().delete_instance()
        
        result['success'] = True
        result['message'] = 'User deleted'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result