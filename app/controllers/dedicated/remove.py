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
from app.utils.variables import DEFAULT_RESULT_TEMPLATE
from app.utils.databases import postgres_db

class RemoveThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function_route, entry=None):
        super().__init__()
        self.function_route = function_route
        self.entry = entry
    
    def run(self):
        result = DEFAULT_RESULT_TEMPLATE.copy()
        
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
        logging.info('result', json.dumps(result, indent=4))

# add function here
def remove_item_prices_by_id(entry=object, result=object):
    pass
def remove_members_by_id(entry=object, result=object):
    pass
def remove_promos_by_id(entry=object, result=object):
    pass
def remove_rewards_by_id(entry=object, result=object):
    pass
def remove_users_by_id(entry=object, result=object):
    pass