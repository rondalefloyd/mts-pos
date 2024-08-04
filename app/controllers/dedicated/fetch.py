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
    Stocks,
    Items,
    ItemPrices,
)
from app.utils.databases import postgres_db


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
            'dictData': {},
            'listData': [],
        }
        
        try:
            with postgres_db:
                if self.function_route == 'fetch_all_organizations_data':
                    result = fetch_all_organizations_data(self.entry, result)
                elif self.function_route == 'fetch_all_promos_data':
                    result = fetch_all_promos_data(self.entry, result)
                elif self.function_route == 'fetch_all_items_related_data':
                    result = fetch_all_items_related_data(self.entry, result)
                elif self.function_route == 'fetch_all_stocks_data_by_keyword_in_pagination':
                    result = fetch_all_stocks_data_by_keyword_in_pagination(self.entry, result)
                elif self.function_route == 'fetch_all_items_related_data_by_keyword_in_pagination':
                    result = fetch_all_items_related_data_by_keyword_in_pagination(self.entry, result)
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
            result['listData'].append({
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
            result['listData'].append({
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
    try:
        itemTypes = ItemTypes.select().order_by(ItemTypes.UpdateTs.desc())
        brands = Brands.select().order_by(Brands.UpdateTs.desc())
        suppliers = Suppliers.select().order_by(Suppliers.UpdateTs.desc())
        
        result['success'] = True
        dictData = result['dictData'] = {
            'itemTypes': [],
            'brands': [],
            'suppliers': [],
        }
        for itemType in itemTypes:
            dictData['itemTypes'].append({
                'id': itemType.Id,
                'itemTypeName': itemType.ItemTypeName,
                'updateTs': itemType.UpdateTs,
            })
        for brand in brands:
            dictData['brands'].append({
                'id': brand.Id,
                'brandName': brand.BrandName,
                'updateTs': brand.UpdateTs,
            })
        for supplier in suppliers:
            dictData['suppliers'].append({
                'id': supplier.Id,
                'supplierName': supplier.SupplierName,
                'updateTs': supplier.UpdateTs,
            })
        return result

    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_stocks_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        stocks = Stocks.select().where(
            (Stocks.OnHand.cast('TEXT').like(keyword)) |
            (Stocks.Available.cast('TEXT').like(keyword)) |
            (Stocks.UpdateTs.cast('TEXT').like(keyword))
        ).order_by(Stocks.UpdateTs.desc())
        
        total_count = stocks.count()
        paginated_stocks = stocks.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for stocks in paginated_stocks:
            result['listData'].append({
                'id': stocks.Id,
                'onHand': stocks.OnHand,
                'available': stocks.Available,
                'updateTs': stocks.UpdateTs,
            })
        
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_items_related_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        item_prices = (ItemPrices.select(
            ItemPrices,
            Items,
            Promos,
            ItemTypes,
            Brands,
            Suppliers,
            SalesGroups,
            Stocks,
        ).join(Items, JOIN.LEFT_OUTER, on=(ItemPrices.ItemId == Items.Id)
        ).join(Promos, JOIN.LEFT_OUTER, on=(ItemPrices.PromoId == Promos.Id)
        ).join(ItemTypes, JOIN.LEFT_OUTER, on=(Items.ItemTypeId == ItemTypes.Id)
        ).join(Brands, JOIN.LEFT_OUTER, on=(Items.BrandId == Brands.Id)
        ).join(Suppliers, JOIN.LEFT_OUTER, on=(Items.SupplierId == Suppliers.Id)
        ).join(SalesGroups, JOIN.LEFT_OUTER, on=(Items.SalesGroupId == SalesGroups.Id)
        ).join(Stocks, JOIN.LEFT_OUTER, on=(Items.SalesGroupId == Stocks.Id)
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
            (Items.StockId.cast('TEXT').like(keyword)) |
            (ItemPrices.UpdateTs.cast('TEXT').like(keyword))
        ).order_by(ItemPrices.UpdateTs.desc(), ItemPrices.EffectiveDate.desc()))
        
        total_count = item_prices.count()
        paginated_item_prices = item_prices.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for item_price in paginated_item_prices:
            result['listData'].append({
                'id': item_price.Id,
                'itemid': item_price.ItemId.Id,
                'itemName': item_price.ItemId.ItemName,
                'barcode': item_price.ItemId.Barcode,
                'expireDate': item_price.ItemId.ExpireDate,
                'itemTypeName': item_price.ItemId.ItemTypeId.ItemTypeName,
                'brandName': item_price.ItemId.BrandId.BrandName,
                'supplierName': item_price.ItemId.SupplierId.SupplierName,
                'salesGroupName': item_price.ItemId.SalesGroupId.SalesGroupName,
                'capital': item_price.Capital,
                'price': item_price.Price,
                'discount': item_price.Discount,
                'effectiveDate': item_price.EffectiveDate,
                'promoName': item_price.PromoId.PromoName if item_price.PromoId else None,
                'stockId': item_price.ItemId.StockId.Id if item_price.ItemId.StockId else None,
                'updateTs': item_price.UpdateTs,
            })
            
        return result
    
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result

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
        result['dictData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for member in paginated_members:
            result['listData'].append({
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
        result['dictData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for promo in paginated_promos:
            result['listData'].append({
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
        result['dictData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for reward in paginated_rewards:
            result['listData'].append({
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
        result['dictData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for user in paginated_users:
            result['listData'].append({
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