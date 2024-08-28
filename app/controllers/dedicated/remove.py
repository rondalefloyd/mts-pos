import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import *
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
                if self.function_route == 'remove_item_price_by_id':
                    result = remove_item_price_by_id(self.entry, result)
                elif self.function_route == 'remove_stock_by_id':
                    result = remove_stock_by_id(self.entry, result)
                elif self.function_route == 'remove_stock_by_id':
                    result = remove_member_by_id(self.entry, result)
                elif self.function_route == 'remove_promo_by_id':
                    result = remove_promo_by_id(self.entry, result)
                elif self.function_route == 'remove_reward_by_id':
                    result = remove_reward_by_id(self.entry, result)
                elif self.function_route == 'remove_user_by_id':
                    result = remove_user_by_id(self.entry, result)
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
        # print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))

# add function here
def remove_item_price_by_id(entry=None, result=None):
    try:
        itemPrice = ItemPrice.select().where(ItemPrice.Id == entry['itemPriceId'])
        
        if not itemPrice.exists():
            result['message'] = 'ItemPrice does not exists'
            return
        
        itemPrice = itemPrice.get_or_none().delete_instance()
        
        result['success'] = True
        result['message'] = 'ItemPrice deleted'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def remove_stock_by_id(entry=None, result=None):
    try:
        stock = Stock.select().where(Stock.Id == entry['id'])
        
        if not stock.exists():
            result['message'] = 'Stock does not exists'
            return
        
        stock = stock.get_or_none().delete_instance()
        
        result['success'] = True
        result['message'] = 'Stock deleted'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result

def remove_member_by_id(entry=None, result=None):
    try:
        member = Member.select().where(Member.Id == entry['id'])
        
        if not member.exists():
            result['message'] = 'Member does not exists'
            return
        
        member = member.get_or_none().delete_instance()
        
        result['success'] = True
        result['message'] = 'Member deleted'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def remove_promo_by_id(entry=None, result=None):
    try:
        promo = Promo.select().where(Promo.Id == entry['id'])
        
        if not promo.exists():
            result['message'] = 'Promo does not exists'
            return
        
        promo = promo.get_or_none().delete_instance()
        
        result['success'] = True
        result['message'] = 'Promo deleted'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def remove_reward_by_id(entry=None, result=None):
    try:
        reward = Reward.select().where(Reward.Id == entry['id'])
        
        if not reward.exists():
            result['message'] = 'Reward does not exists'
            return
        
        reward = reward.get_or_none().delete_instance()
        
        result['success'] = True
        result['message'] = 'Reward deleted'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def remove_user_by_id(entry=None, result=None):
    try:
        user = User.select().where(User.Id == entry['id'])
        
        if not user.exists():
            result['message'] = 'User does not exists'
            return
        
        user = user.get_or_none().delete_instance()
        
        result['success'] = True
        result['message'] = 'User deleted'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result