import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import (
    Users, 
    UserSessionInfos, 
    Organizations,
    Members,
    Promos,
    Rewards,
    ItemTypes,
    Brands,
    Suppliers,
    SalesGroups,
    Items,
    ItemPrices,
    Stocks,
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
            'message': 'N/A',
        }
        
        try:
            with postgres_db:
                if self.function_route == 'register_items':
                    message = register_items(self.entry)
                elif self.function_route == 'register_members':
                    message = register_members(self.entry)
                elif self.function_route == 'register_promos':
                    message = register_promos(self.entry)
                elif self.function_route == 'register_rewards':
                    message = register_rewards(self.entry)
                elif self.function_route == 'register_users':
                    message = register_users(self.entry)
                elif self.function_route == 'register_organizations':
                    message = register_organizations(self.entry)
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
def register_items(entry=object):
    pass
def register_members(entry=object):
    pass
def register_promos(entry=object):
    pass
def register_rewards(entry=object):
    pass
def register_users(entry=object):
    pass
def register_organizations(entry=object):
    pass