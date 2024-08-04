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
from app.utils.databases import postgres_db

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
            'oneData': {},
            'manyData': [],
        }
         
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
        print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))

# add function here
def register_items(entry=None, result=None):
    pass
def register_members(entry=None, result=None):
    try:
        member = Members.select().where(
            (Members.OrganizationId == Organizations.get(Organizations.OrganizationName == entry['organizationName']).Id) &
            (Members.MemberName == entry['memberName']) &
            (Members.BirthDate == entry['birthDate']) &
            (Members.Address == entry['address']) &
            (Members.MobileNumber == entry['mobileNumber']) &
            (Members.Points == entry['points'])
        )
        
        if member.exists():
            result['message'] = 'Member already exists'
            return result
        
        member = Members.create(
            OrganizationId=Organizations.get(Organizations.OrganizationName == entry['organizationName']).Id,
            MemberName=entry['memberName'],
            BirthDate=entry['birthDate'],
            Address=entry['address'],
            MobileNumber=entry['mobileNumber'],
            Points=entry['points'],
        )
        
        result['success'] = True
        result['message'] = 'Member added'
        return result

    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def register_promos(entry=None, result=None):
    try:
        promo = Promos.select().where(
            (Promos.PromoName == entry['promoName']) &
            (Promos.DiscountRate == entry['discountRate']) &
            (Promos.Description == entry['description'])
        )
        
        if promo.exists():
            result['message'] = 'Promo already exists'
        
        promo = Promos.create(
            PromoName=entry['promoName'],
            DiscountRate=entry['discountRate'],
            Description=entry['description'],
        )
        
        result['success'] = True
        result['message'] = 'Promo added'
        return result

    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def register_rewards(entry=None, result=None):
    try:
        reward = Rewards.select().where(
            (Rewards.RewardName == entry['rewardName']) &
            (Rewards.Points == entry['points']) &
            (Rewards.Target == entry['target']) &
            (Rewards.Description == entry['description'])
        )
        
        if reward.exists():
            result['message'] = 'Reward already exists'
        
        reward = Rewards.create(
            RewardName=entry['rewardName'],
            Points=entry['points'],
            Target=entry['target'],
            Description=entry['description'],
        )
        
        result['success'] = True
        result['message'] = 'Reward added'
        return result

    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def register_users(entry=None, result=None):
    try:
        user = Users.select().where(
            (Users.OrganizationId == Organizations.get(Organizations.OrganizationName == entry['organizationName']).Id) &
            (Users.UserName == entry['userName']) &
            (Users.AccessCode == entry['accessCode']) &
            (Users.FullName == entry['fullName']) &
            (Users.BirthDate == entry['birthDate']) &
            (Users.MobileNumber == entry['mobileNumber']) &
            (Users.AccessLevel == entry['accessLevel'])
        )
        
        if user.exists():
            result['message'] = 'User already exists'
            return result
        
        user = Users.create(
            OrganizationId=Organizations.get(Organizations.OrganizationName == entry['organizationName']).Id,
            UserName=entry['userName'],
            AccessCode=entry['accessCode'],
            FullName=entry['fullName'],
            BirthDate=entry['birthDate'],
            MobileNumber=entry['mobileNumber'],
            AccessLevel=entry['accessLevel'],
        )
        
        userSessionInfo = UserSessionInfos.create(
            UserId=user.Id,
            ActiveStatus=0,
            LastLoginTs=datetime.now(),
        )
        
        result['success'] = True
        result['message'] = 'User added'
        return result

    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def register_organizations(entry=None, result=None):
    try:
        organization = Organizations.select().where(
            (Organizations.TaxId == entry['taxId']) &
            (Organizations.OrganizationName == entry['organizationName']) &
            (Organizations.Address == entry['address']) &
            (Organizations.MobileNumber == entry['mobileNumber']) &
            (Organizations.AccessCode == entry['accessCode'])
        )
        
        if organization.exists():
            result['message'] = 'Organization already exists'
        
        organization = Organizations.create(
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