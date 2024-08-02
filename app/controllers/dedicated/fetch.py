import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import (
    Users, 
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
)
from app.utils.database import postgres_db

logging.basicConfig(level=logging.INFO)

class FetchThread(QThread):
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
                if self.function_route == 'fetch_all_items_related_data':
                    message = fetch_all_items_related_data(self.entry)
                elif self.function_route == 'fetch_all_promos_data':
                    message = fetch_all_promos_data(self.entry)
                elif self.function_route == 'fetch_all_items_related_data':
                    message = fetch_all_items_related_data(self.entry)
                elif self.function_route == 'fetch_all_members_data_by_keyword_in_pagination':
                    message = fetch_all_members_data_by_keyword_in_pagination(self.entry)
                elif self.function_route == 'fetch_all_promos_data_by_keyword_in_pagination':
                    message = fetch_all_promos_data_by_keyword_in_pagination(self.entry)
                elif self.function_route == 'fetch_all_rewards_data_by_keyword_in_pagination':
                    message = fetch_all_rewards_data_by_keyword_in_pagination(self.entry)
                elif self.function_route == 'fetch_all_users_data_by_keyword_in_pagination':
                    message = fetch_all_users_data_by_keyword_in_pagination(self.entry)
                elif self.function_route == 'fetch_all_organizations_data_by_keyword_in_pagination':
                    message = fetch_all_organizations_data_by_keyword_in_pagination(self.entry)
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
def fetch_all_items_related_data(entry=object):
    pass
def fetch_all_promos_data(entry=object):
    pass
def fetch_all_items_related_data(entry=object):
    pass
def fetch_all_members_data_by_keyword_in_pagination(entry=object):
    pass
def fetch_all_promos_data_by_keyword_in_pagination(entry=object):
    pass
def fetch_all_rewards_data_by_keyword_in_pagination(entry=object):
    pass
def fetch_all_users_data_by_keyword_in_pagination(entry=object):
    pass
def fetch_all_organizations_data_by_keyword_in_pagination(entry=object):
    pass