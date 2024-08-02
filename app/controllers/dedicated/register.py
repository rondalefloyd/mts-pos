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
from app.utils.variables import DEFAULT_RESULT_TEMPLATE
from app.utils.databases import postgres_db

logging.basicConfig(level=logging.INFO)

class RegisterThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function_route, entry=None):
        super().__init__()
        self.function_route = function_route
        self.entry = entry
    
    def run(self):
        result = DEFAULT_RESULT_TEMPLATE.copy()
         
        try:
            with postgres_db:
                if self.function_route == 'register_items':
                    result = register_items(self.entry, result)
                elif self.function_route == 'register_members':
                    result = register_members(self.entry, result)
                elif self.function_route == 'register_promos':
                    result = register_promos(self.entry, result)
                elif self.function_route == 'register_rewards':
                    result = register_rewards(self.entry, result)
                elif self.function_route == 'register_users':
                    result = register_users(self.entry, result)
                elif self.function_route == 'register_organizations':
                    result = register_organizations(self.entry, result)
                else:
                    result['message'] = f"'{self.function_route}' is an invalid function..."
                        
            logging.info('database operation done...')
            
        except Exception as exception:
            result['message'] = f"An error occured: {exception}"
            postgres_db.rollback()
            logging.error('exception: %s', exception)
            logging.info('database operation rolled back...')
            
        finally:
            postgres_db.close()
            logging.info('database closed...')
            
        self.finished.emit(result)
        logging.info('result', json.dumps(result, indent=4))

# add function here
def register_items(entry=object, result=object):
    pass
def register_members(entry=object, result=object):
    pass
def register_promos(entry=object, result=object):
    pass
def register_rewards(entry=object, result=object):
    pass
def register_users(entry=object, result=object):
    try:
        users = Users.select().where(
            (Users.OrganizationId == Organizations.get(Organizations.OrganizationName == entry['organizationName']).Id) &
            (Users.UserName == entry['userName']) &
            (Users.AccessCode == entry['accessCode']) &
            (Users.FullName == entry['fullName']) &
            (Users.BirthDate == entry['birthDate']) &
            (Users.MobileNumber == entry['mobileNumber']) &
            (Users.AccessLevel == entry['accessLevel'])
        )
        
        if users.exists():
            result['message'] = 'User already exists'
            return result
        
        users = Users.create(
            OrganizationId=entry['organizationName'],
            UserName=entry['userName'],
            AccessCode=entry['accessCode'],
            FullName=entry['fullName'],
            BirthDate=entry['birthDate'],
            MobileNumber=entry['mobileNumber'],
            AccessLevel=entry['accessLevel'],
        )
        
        userSessionInfos = UserSessionInfos.create(
            UserId=users.Id,
            ActiveStatus=0,
            LastLoginTs=entry['lastLoginTs'],
        )
        
        result['success'] = True
        result['message'] = 'User added'
        return result

    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
    
def register_organizations(entry=object, result=object):
    try:
        organizations = Organizations.select().where(
            (Organizations.TaxId == entry['taxId']) &
            (Organizations.OrganizationName == entry['organizationName']) &
            (Organizations.Address == entry['address']) &
            (Organizations.MobileNumber == entry['mobileNumber']) &
            (Organizations.AccessCode == entry['accessCode'])
        )
        
        if organizations.exists():
            result['message'] = 'Organization already exists'
        
        organizations = Organizations.create(
            TaxId=entry['taxId'],
            OrganizationName=entry['organizationName'],
            Address=entry['address'],
            MobileNumber=entry['mobileNumber'],
            AccessCode=entry['accessCode'],
        )
        
        result['success'] = True
        result['message'] = 'Organization added'
        return result

    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result