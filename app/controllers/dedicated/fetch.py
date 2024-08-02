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
from app.utils.variables import DEFAULT_RESULT_TEMPLATE
from app.utils.databases import postgres_db

logging.basicConfig(level=logging.INFO)

class FetchThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function_route, entry=None):
        super().__init__()
        self.function_route = function_route
        self.entry = entry
    
    def run(self):
        result = DEFAULT_RESULT_TEMPLATE.copy()
        
        try:
            with postgres_db:
                if self.function_route == 'fetch_all_organizations_data':
                    result = fetch_all_organizations_data(self.entry, result)
                elif self.function_route == 'fetch_all_promos_data':
                    result = fetch_all_promos_data(self.entry, result)
                elif self.function_route == 'fetch_all_items_related_data':
                    result = fetch_all_items_related_data(self.entry, result)
                elif self.function_route == 'fetch_all_members_data_by_keyword_in_pagination':
                    result = fetch_all_members_data_by_keyword_in_pagination(self.entry, result)
                elif self.function_route == 'fetch_all_promos_data_by_keyword_in_pagination':
                    result = fetch_all_promos_data_by_keyword_in_pagination(self.entry, result)
                elif self.function_route == 'fetch_all_rewards_data_by_keyword_in_pagination':
                    result = fetch_all_rewards_data_by_keyword_in_pagination(self.entry, result)
                elif self.function_route == 'fetch_all_users_data_by_keyword_in_pagination':
                    result = fetch_all_users_data_by_keyword_in_pagination(self.entry, result)
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
# TODO: fix this
def fetch_all_organizations_data(entry=object, result=object):
    try:
        organizations = Organizations.select().order_by(Organizations.UpdateTs).desc()
        
        if not organizations.exists():
            result['message'] = 'Organization does not exists'
        
        organizations = organizations.all()

        result['success'] = True
        for organization in organizations:
            result['many_data'].append({
                'taxId': organization.TaxId,
                'organizationName': organization.OrganizationName,
                'address': organization.Address,
                'mobileNumber': organization.MobileNumber,
                'accessCode': organization.AccessCode,
            })
        return result

    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    pass
def fetch_all_promos_data(entry=object, result=object):
    pass
def fetch_all_items_related_data(entry=object, result=object):
    pass
def fetch_all_members_data_by_keyword_in_pagination(entry=object, result=object):
    pass
def fetch_all_promos_data_by_keyword_in_pagination(entry=object, result=object):
    pass
def fetch_all_rewards_data_by_keyword_in_pagination(entry=object, result=object):
    pass
def fetch_all_users_data_by_keyword_in_pagination(entry=object, result=object):
    pass