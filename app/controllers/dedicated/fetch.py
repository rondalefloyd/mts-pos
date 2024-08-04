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
from app.utils.databases import postgres_db

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
            'oneData': {},
            'manyData': [],
        }
        
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
        # TODO: continue working on ITEMS
        print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))

# add function here
def fetch_all_organizations_data(entry=None, result=None):
    try:
        organizations = Organizations.select().order_by(Organizations.UpdateTs.desc())
        
        if not organizations.exists():
            result['message'] = 'Organization does not exists'
        
        result['success'] = True
        for organization in organizations:
            result['manyData'].append({
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

def fetch_all_promos_data(entry=None, result=None):
    try:
        promos = Promos.select().order_by(Promos.UpdateTs.desc())
        
        if not promos.exists():
            result['message'] = 'Organization does not exists'
        
        result['success'] = True
        for promo in promos:
            result['manyData'].append({
                'id': promo.Id,
                'promoName': promo.PromoName,
                'discountRate': promo.DiscountRate,
                'description': promo.Description,
                'updateTs': promo.UpdateTs,
            })
        return result

    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_items_related_data(entry=None, result=None):
    pass
def fetch_all_members_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        members = Members.select().where(
            (Members.OrganizationId == Organizations.get(Organizations.OrganizationName == entry['organizationName']).Id) &
            ((Members.MemberName.cast('TEXT').like(keyword)) |
            (Members.BirthDate.cast('TEXT').like(keyword)) |
            (Members.Address.cast('TEXT').like(keyword)) |
            (Members.MobileNumber.cast('TEXT').like(keyword)) |
            (Members.Points.cast('TEXT').like(keyword)) |
            (Members.UpdateTs.cast('TEXT').like(keyword)))
        ).order_by(Members.UpdateTs.desc())
        
        total_count = members.count()
        paginated_members = members.limit(limit).offset(offset)
        
        result['success'] = True
        result['oneData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for member in paginated_members:
            result['manyData'].append({
                'id': member.Id,
                'organizationId': member.OrganizationId,
                'memberName': member.MemberName,
                'birthDate': member.BirthDate,
                'address': member.Address,
                'mobileNumber': member.MobileNumber,
                'points': member.Points,
                'updateTs': member.UpdateTs,
            })
        
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_promos_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        promos = Promos.select().where(
            (Promos.PromoName.cast('TEXT').like(keyword)) |
            (Promos.DiscountRate.cast('TEXT').like(keyword)) |
            (Promos.Description.cast('TEXT').like(keyword)) |
            (Promos.UpdateTs.cast('TEXT').like(keyword))
        ).order_by(Promos.UpdateTs.desc())
        
        total_count = promos.count()
        paginated_promos = promos.limit(limit).offset(offset)
        
        result['success'] = True
        result['oneData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for promo in paginated_promos:
            result['manyData'].append({
                'id': promo.Id,
                'promoName': promo.PromoName,
                'discountRate': promo.DiscountRate,
                'description': promo.Description,
                'updateTs': promo.UpdateTs,
            })
        
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_rewards_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        rewards = Rewards.select().where(
            (Rewards.RewardName.cast('TEXT').like(keyword)) |
            (Rewards.Points.cast('TEXT').like(keyword)) |
            (Rewards.Target.cast('TEXT').like(keyword)) |
            (Rewards.Description.cast('TEXT').like(keyword)) |
            (Rewards.UpdateTs.cast('TEXT').like(keyword))
        ).order_by(Rewards.UpdateTs.desc())
        
        total_count = rewards.count()
        paginated_rewards = rewards.limit(limit).offset(offset)
        
        result['success'] = True
        result['oneData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for reward in paginated_rewards:
            result['manyData'].append({
                'id': reward.Id,
                'rewardName': reward.RewardName,
                'points': reward.Points,
                'target': reward.Target,
                'description': reward.Description,
                'updateTs': reward.UpdateTs,
            })
        
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_users_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        users = Users.select().where(
            (Users.OrganizationId == Organizations.get(Organizations.OrganizationName == entry['organizationName']).Id) &
            ((Users.UserName.cast('TEXT').like(keyword)) |
            (Users.AccessCode.cast('TEXT').like(keyword)) |
            (Users.FullName.cast('TEXT').like(keyword)) |
            (Users.BirthDate.cast('TEXT').like(keyword)) |
            (Users.MobileNumber.cast('TEXT').like(keyword)) |
            (Users.AccessLevel.cast('TEXT').like(keyword)) |
            (Users.UpdateTs.cast('TEXT').like(keyword)))
        ).order_by(Users.UpdateTs.desc())
        
        total_count = users.count()
        paginated_users = users.limit(limit).offset(offset)
        
        result['success'] = True
        result['oneData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for user in paginated_users:
            result['manyData'].append({
                'id': user.Id,
                'userName': user.UserName,
                'accessCode': user.AccessCode,
                'fullName': user.FullName,
                'birthDate': user.BirthDate,
                'mobileNumber': user.MobileNumber,
                'accessLevel': user.AccessLevel,
                'updateTs': user.UpdateTs,
            })
        
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result