import os, sys, logging, math
from peewee import *
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
from app.controllers.common.validator import entry_has_value
from app.controllers.common.messages import (
    exception_error_message,
    integrity_error_message,
    function_route_not_exist,
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
                match self.function_route:
                    case 'pos/fetch/user/all':
                        result = fetch_user(self.entry)
                    case 'pos/fetch/promo/all':
                        result = fetch_promo()
                    case 'pos/fetch/promo/promo-name':
                        result = fetch_promo_by_promo_name(self.entry)
                    case 'pos/fetch/organization/all':
                        result = fetch_organization()
                    case 'pos/fetch/itemtype-brand-supplier-salesgroup/all':
                        result = fetch_itemtype_brand_supplier_salesgroup()
                    case 'pos/fetch/user/all/keyword/paginated':
                        result = fetch_user_with_pagination_by_keyword(self.entry)
                    case 'pos/fetch/members/all/keyword/paginated':
                        result = fetch_members_with_pagination_by_keyword(self.entry)
                    case 'pos/fetch/promos/all/keyword/paginated':
                        result = fetch_promos_with_pagination_by_keyword(self.entry)
                    case 'pos/fetch/rewards/all/keyword/paginated':
                        result = fetch_rewards_with_pagination_by_keyword(self.entry)
                    case 'pos/fetch/items/all/keyword/paginated':
                        result = fetch_items_with_pagination_by_keyword(self.entry)
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

def fetch_user(entry):
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': []
    }
    
    try:
        users = Users.select().order_by(
            (Users.OrganizationId == entry['organizationId']) &
            (Users.UpdateTs.desc())
        )
        
        for user in users:
            result['success'] = True
            result['message'] = 'Fetch successful.'
            result['data'].append({
                'id': user.Id,
                'organizationId': user.OrganizationId,
                'userName': user.UserName,
                'accessCode': user.AccessCode,
                'fullName': user.FullName,
                'birthDate': user.BirthDate,
                'mobileNumber': user.MobileNumber,
                'accessLevel': user.AccessLevel,
                'updateTs': user.UpdateTs,
            })
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def fetch_promo():
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': []
    }
    
    try:
        promos = Promos.select().order_by(Promos.UpdateTs.desc())
        
        for promo in promos:
            result['success'] = True
            result['message'] = 'Fetch successful.'
            result['data'].append({
                'id': promo.Id,
                'promoName': promo.PromoName,
                'discountRate': promo.DiscountRate,
                'description': promo.Description,
                'updateTs': promo.UpdateTs,
            })
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def fetch_promo_by_promo_name(entry):
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': {
            'id': None,
            'promoName': None,
            'discountRate': None,
            'description': None,
            'updateTs': None,
        }
    }
    
    try:
        promos = Promos.select().where(Promos.PromoName == entry['promoName']).order_by(Promos.UpdateTs.desc())
        
        if not promos.exists():
            result['message'] = 'Fetch failed. Promo not found.'
            return result
        
        promos = promos.first()
        
        result['success'] = True
        result['message'] = 'Fetch successful.'
        result['data'] = {
            'id': promos.Id,
            'promoName': promos.PromoName,
            'discountRate': promos.DiscountRate,
            'description': promos.Description,
            'updateTs': promos.UpdateTs,
        }
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    print(result)
    return result


def fetch_organization():
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': []
    }
    
    try:
        organizations = Organizations.select().order_by(Organizations.UpdateTs.desc())
        
        for organization in organizations:
            result['success'] = True
            result['message'] = 'Fetch successful.'
            result['data'].append({
                'id': organization.Id,
                'taxId': organization.TaxId,
                'organizationName': organization.OrganizationName,
                'address': organization.Address,
                'mobileNumber': organization.MobileNumber,
                'accessCode': organization.AccessCode,
                'updateTs': organization.UpdateTs,
            })
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def fetch_itemtype_brand_supplier_salesgroup():
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': {
            'itemTypes': [],
            'brands': [],
            'suppliers': [],
            'salesGroups': [],
        }
    }
    
    try:
        itemTypes = ItemTypes.select().order_by(ItemTypes.UpdateTs.desc())
        brands = Brands.select().order_by(Brands.UpdateTs.desc())
        suppliers = Suppliers.select().order_by(Suppliers.UpdateTs.desc())
        salesGroups = SalesGroups.select().order_by(SalesGroups.UpdateTs.desc())
        
        for itemType in itemTypes:
            result['data']['itemTypes'].append({
                'id': itemType.Id,
                'itemTypeName': itemType.ItemTypeName,
                'updateTs': itemType.UpdateTs,
            })
            
        for brand in brands:
            result['data']['brands'].append({
                'id': brand.Id,
                'brandName': brand.BrandName,
                'updateTs': brand.UpdateTs,
            })
            
        for supplier in suppliers:
            result['data']['suppliers'].append({
                'id': supplier.Id,
                'supplierName': supplier.SupplierName,
                'updateTs': supplier.UpdateTs,
            })
            
        for salesGroup in salesGroups:
            result['data']['salesGroups'].append({
                'id': salesGroup.Id,
                'salesGroupName': salesGroup.SalesGroupName,
                'updateTs': salesGroup.UpdateTs,
            })
            
            
        result['success'] = True
        result['message'] = 'Fetch successful.'
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result


def fetch_user_with_pagination_by_keyword(entry):
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': [],
        'totalPages': 1,
    }
    
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        users = Users.select().where(
            (Users.OrganizationId == entry['organizationId']) &
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
        
        for user in paginated_users:
            result['data'].append({
                'id': user.Id,
                'userName': user.UserName,
                'accessCode': user.AccessCode,
                'fullName': user.FullName,
                'birthDate': user.BirthDate,
                'mobileNumber': user.MobileNumber,
                'accessLevel': user.AccessLevel,
                'updateTs': user.UpdateTs,
            })
        
        result['totalPages'] = math.ceil(total_count / limit)
        
        result['success'] = True
        result['message'] = 'Fetch successful.'
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def fetch_members_with_pagination_by_keyword(entry):
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': [],
        'totalPages': 1,
    }
    
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        members = Members.select().where(
            (Members.OrganizationId == entry['organizationId']) &
            ((Members.MemberName.cast('TEXT').like(keyword)) |
            (Members.BirthDate.cast('TEXT').like(keyword)) |
            (Members.Address.cast('TEXT').like(keyword)) |
            (Members.MobileNumber.cast('TEXT').like(keyword)) |
            (Members.Points.cast('TEXT').like(keyword)) |
            (Members.UpdateTs.cast('TEXT').like(keyword)))
        ).order_by(Members.UpdateTs.desc())
        
        total_count = members.count()
        
        paginated_members = members.limit(limit).offset(offset)
        
        for member in paginated_members:
            result['data'].append({
                'id': member.Id,
                'organizationId': member.OrganizationId,
                'memberName': member.MemberName,
                'birthDate': member.BirthDate,
                'address': member.Address,
                'mobileNumber': member.MobileNumber,
                'points': member.Points,
                'updateTs': member.UpdateTs,
            })
        
        result['totalPages'] = math.ceil(total_count / limit)
        
        result['success'] = True
        result['message'] = 'Fetch successful.'
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def fetch_promos_with_pagination_by_keyword(entry):
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': [],
        'totalPages': 1,
    }
    
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
        
        for promo in paginated_promos:
            result['data'].append({
                'id': promo.Id,
                'promoName': promo.PromoName,
                'discountRate': promo.DiscountRate,
                'description': promo.Description,
                'updateTs': promo.UpdateTs,
            })
        
        result['totalPages'] = math.ceil(total_count / limit)
        
        result['success'] = True
        result['message'] = 'Fetch successful.'
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

def fetch_rewards_with_pagination_by_keyword(entry):
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': [],
        'totalPages': 1,
    }
    
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
        
        for reward in paginated_rewards:
            result['data'].append({
                'id': reward.Id,
                'rewardName': reward.RewardName,
                'points': reward.Points,
                'target': reward.Target,
                'description': reward.Description,
                'updateTs': reward.UpdateTs,
            })
        
        result['totalPages'] = math.ceil(total_count / limit)
        
        result['success'] = True
        result['message'] = 'Fetch successful.'
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    return result

# TODO: fix something wrong with how the data is being returned or retrieved from the query
def fetch_items_with_pagination_by_keyword(entry):
    result = {
        'success': False,
        'message': 'Fetch failed.',
        'data': [],
        'totalPages': 1,
    }
    
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        itemPrices = (ItemPrices.select(
            ItemPrices,
            Items,
            Promos,
            ItemTypes,
            Brands,
            Suppliers,
            SalesGroups,
        ).join(Items, JOIN.LEFT_OUTER, on=(ItemPrices.ItemId == Items.Id)
        ).join(Promos, JOIN.LEFT_OUTER, on=(ItemPrices.PromoId == Promos.Id)
        ).join(ItemTypes, JOIN.LEFT_OUTER, on=(Items.ItemTypeId == ItemTypes.Id)
        ).join(Brands, JOIN.LEFT_OUTER, on=(Items.BrandId == Brands.Id)
        ).join(Suppliers, JOIN.LEFT_OUTER, on=(Items.SupplierId == Suppliers.Id)
        ).join(SalesGroups, JOIN.LEFT_OUTER, on=(Items.SalesGroupId == SalesGroups.Id)
        ).where(
            (Items.ItemName.cast('TEXT').like(keyword)) |
            (Items.Barcode.cast('TEXT').like(keyword)) |
            (Items.ExpireDate.cast('TEXT').like(keyword)) |
            (ItemTypes.ItemTypeName.cast('TEXT').like(keyword)) |
            (Brands.BrandName.cast('TEXT').like(keyword)) |
            (Suppliers.SupplierName.cast('TEXT').like(keyword)) |
            (SalesGroups.SalesGroupName.cast('TEXT').like(keyword)) |
            (ItemPrices.EffectiveDate.cast('TEXT').like(keyword)) |
            (Promos.PromoName.cast('TEXT').like(keyword)) |
            (ItemPrices.UpdateTs.cast('TEXT').like(keyword))
        ).order_by(ItemPrices.UpdateTs.desc(), ItemPrices.EffectiveDate.desc()))
        
        
        total_count = itemPrices.count()
        
        paginated_itemPrices = itemPrices.limit(limit).offset(offset)
        
        for itemPrice in paginated_itemPrices:
            result['data'].append({
                'id': itemPrice.Id,
                'itemid': itemPrice.ItemId.Id,
                'itemName': itemPrice.ItemId.ItemName,
                'barcode': itemPrice.ItemId.Barcode,
                'expireDate': itemPrice.ItemId.ExpireDate,
                
                'itemTypeName': itemPrice.ItemId.ItemTypeId.ItemTypeName,
                'brandName': itemPrice.ItemId.BrandId.BrandName,
                'supplierName': itemPrice.ItemId.SupplierId.SupplierName,
                'salesGroupName': itemPrice.ItemId.SalesGroupId.SalesGroupName,
                
                'capital': itemPrice.Capital,
                'price': itemPrice.Price,
                'discount': itemPrice.Discount,
                'effectiveDate': itemPrice.EffectiveDate,
                
                'promoName': itemPrice.PromoId.PromoName if itemPrice.PromoId else None,
                
                'updateTs': itemPrice.UpdateTs,
            })
        
        result['totalPages'] = math.ceil(total_count / limit)
        
        result['success'] = True
        result['message'] = 'Fetch successful.'
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        
    print("result:", result)
    return result
