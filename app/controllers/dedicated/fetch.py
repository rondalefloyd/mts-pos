import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import (
    User, 
    Organization,
    Member,
    Promo,
    Reward,
    ItemType,
    Brand,
    Supplier,
    SalesGroup,
    Stock,
    Item,
    ItemPrice,
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
                if self.function_route == 'fetch_all_organization_data':
                    result = fetch_all_organization_data(self.entry, result)
                elif self.function_route == 'fetch_promo_data_by_promo_name':
                    result = fetch_promo_data_by_promo_name(self.entry, result)
                elif self.function_route == 'fetch_all_promo_data':
                    result = fetch_all_promo_data(self.entry, result)
                elif self.function_route == 'fetch_all_item_related_data':
                    result = fetch_all_item_related_data(self.entry, result)
                elif self.function_route == 'fetch_all_stock_data_by_keyword_in_pagination':
                    result = fetch_all_stock_data_by_keyword_in_pagination(self.entry, result)
                elif self.function_route == 'fetch_all_item_price_related_data_by_keyword_in_pagination':
                    result = fetch_all_item_price_related_data_by_keyword_in_pagination(self.entry, result)
                elif self.function_route == 'fetch_all_member_data_by_keyword_in_pagination':
                    result = fetch_all_member_data_by_keyword_in_pagination(self.entry, result)
                elif self.function_route == 'fetch_all_promo_data_by_keyword_in_pagination':
                    result = fetch_all_promo_data_by_keyword_in_pagination(self.entry, result)
                elif self.function_route == 'fetch_all_reward_data_by_keyword_in_pagination':
                    result = fetch_all_reward_data_by_keyword_in_pagination(self.entry, result)
                elif self.function_route == 'fetch_all_user_data_by_keyword_in_pagination':
                    result = fetch_all_user_data_by_keyword_in_pagination(self.entry, result)
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
        print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))

# add function here
def fetch_all_organization_data(entry=None, result=None):
    try:
        organizations = Organization.select().order_by(Organization.UpdateTs.desc())
        
        if not organizations.exists():
            result['message'] = 'Organization does not exists'
            return result
        
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
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result


def fetch_promo_data_by_promo_name(entry=None, result=None):
    try:
        promo = Promo.select().where(Promo.PromoName == entry['promoName']).order_by(Promo.UpdateTs.desc())
        
        if not promo.exists():
            result['message'] = 'Promo does not exists'
            return result
        
        promo = promo.first()
        
        result['success'] = True
        result['dictData'] = {
            'id': promo.Id,
            'promoName': promo.PromoName,
            'discountRate': promo.DiscountRate,
            'description': promo.Description,
            'updateTs': promo.UpdateTs,
        }

        return result

    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result

def fetch_all_promo_data(entry=None, result=None):
    try:
        promos = Promo.select().order_by(Promo.UpdateTs.desc())
        
        if not promos.exists():
            result['message'] = 'Promo does not exists'
            return result
        
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
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_item_related_data(entry=None, result=None):
    try:
        itemTypes = ItemType.select().order_by(ItemType.UpdateTs.desc())
        brands = Brand.select().order_by(Brand.UpdateTs.desc())
        suppliers = Supplier.select().order_by(Supplier.UpdateTs.desc())
        salesGroups = SalesGroup.select().order_by(SalesGroup.UpdateTs.desc())
        
        result['success'] = True
        result['dictData'] = {
            'itemTypes': [],
            'brands': [],
            'suppliers': [],
            'salesGroups': [],
        }
        dictData = result['dictData']
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
        for salesGroup in salesGroups:
            dictData['salesGroups'].append({
                'id': salesGroup.Id,
                'salesGroupName': salesGroup.SalesGroupName,
                'updateTs': salesGroup.UpdateTs,
            })
            
        return result

    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_stock_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        stocks = (Stock.select(
            Stock,
            Item,
        ).join(Item, JOIN.LEFT_OUTER, on=(Stock.ItemId == Item.Id)
        ).join(SalesGroup, JOIN.LEFT_OUTER, on=(Item.SalesGroupId == SalesGroup.Id)
        ).where(
            (Item.ItemName.cast('TEXT').like(keyword)) |
            (SalesGroup.SalesGroupName.cast('TEXT').like(keyword)) |
            (Stock.OnHand.cast('TEXT').like(keyword)) |
            (Stock.Available.cast('TEXT').like(keyword)) |
            (Stock.UpdateTs.cast('TEXT').like(keyword))
        ).order_by(Stock.UpdateTs.desc()))
        
        total_count = stocks.count()
        paginated_stocks = stocks.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for stocks in paginated_stocks:
            result['listData'].append({
                'id': stocks.Id,
                'itemName': stocks.ItemId.ItemName,
                'salesGroup': stocks.ItemId.SalesGroupId.SalesGroupName,
                'onHand': stocks.OnHand,
                'available': stocks.Available,
                'updateTs': stocks.UpdateTs,
            })
        
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_item_price_related_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        item_prices = (ItemPrice.select(
            ItemPrice,
            Item,
            Promo,
            ItemType,
            Brand,
            Supplier,
            SalesGroup,
        ).join(Item, JOIN.LEFT_OUTER, on=(ItemPrice.ItemId == Item.Id)
        ).join(Promo, JOIN.LEFT_OUTER, on=(ItemPrice.PromoId == Promo.Id)
        ).join(ItemType, JOIN.LEFT_OUTER, on=(Item.ItemTypeId == ItemType.Id)
        ).join(Brand, JOIN.LEFT_OUTER, on=(Item.BrandId == Brand.Id)
        ).join(Supplier, JOIN.LEFT_OUTER, on=(Item.SupplierId == Supplier.Id)
        ).join(SalesGroup, JOIN.LEFT_OUTER, on=(Item.SalesGroupId == SalesGroup.Id)
        ).where(
            (Item.ItemName.cast('TEXT').like(keyword)) |
            (Item.Barcode.cast('TEXT').like(keyword)) |
            (Item.ExpireDate.cast('TEXT').like(keyword)) |
            (ItemType.ItemTypeName.cast('TEXT').like(keyword)) |
            (Brand.BrandName.cast('TEXT').like(keyword)) |
            (Supplier.SupplierName.cast('TEXT').like(keyword)) |
            (SalesGroup.SalesGroupName.cast('TEXT').like(keyword)) |
            (ItemPrice.EffectiveDate.cast('TEXT').like(keyword)) |
            (Promo.PromoName.cast('TEXT').like(keyword)) |
            (ItemPrice.UpdateTs.cast('TEXT').like(keyword))
        ).order_by(ItemPrice.UpdateTs.desc(), ItemPrice.EffectiveDate.desc()))
        
        total_count = item_prices.count()
        paginated_item_prices = item_prices.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(total_count / limit) if 0 else 1}
        for item_price in paginated_item_prices:
            item = item_price.ItemId
            itemType = item.ItemTypeId
            brand = item.BrandId
            supplier = item.SupplierId
            salesGroup = item.SalesGroupId
            promo = item_price.PromoId
            stock = Stock.get_or_none(Stock.ItemId == item.Id)
            
            result['listData'].append({
                # ids for editting purpose
                'itemid': item.Id,
                'itemTypeId': itemType.Id,
                'brandId': brand.Id,
                'supplierId': supplier.Id,
                'salesGroupId': salesGroup.Id,
                'itemPriceId': item_price.Id,
                'promoId': promo.Id if promo else None,
                'stockId': stock.Id if stock else None,
                # ids for displaying purpose
                'itemName': item.ItemName,
                'barcode': item.Barcode,
                'expireDate': item.ExpireDate,
                'itemTypeName': itemType.ItemTypeName,
                'brandName': brand.BrandName,
                'supplierName': supplier.SupplierName,
                'salesGroupName': salesGroup.SalesGroupName,
                'capital': item_price.Capital,
                'price': item_price.Price,
                'discount': item_price.Discount,
                'effectiveDate': item_price.EffectiveDate,
                'promoName': promo.PromoName if promo else None,
                'updateTs': item_price.UpdateTs,
            })
            
        return result
    
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result

def fetch_all_member_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        members = Member.select().where(
            (Member.OrganizationId == Organization.get_or_none(Organization.OrganizationName == entry['organizationName']).Id) &
            ((Member.MemberName.cast('TEXT').like(keyword)) |
            (Member.BirthDate.cast('TEXT').like(keyword)) |
            (Member.Address.cast('TEXT').like(keyword)) |
            (Member.MobileNumber.cast('TEXT').like(keyword)) |
            (Member.Points.cast('TEXT').like(keyword)) |
            (Member.UpdateTs.cast('TEXT').like(keyword)))
        ).order_by(Member.UpdateTs.desc())
        
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
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_promo_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        promos = Promo.select().where(
            (Promo.PromoName.cast('TEXT').like(keyword)) |
            (Promo.DiscountRate.cast('TEXT').like(keyword)) |
            (Promo.Description.cast('TEXT').like(keyword)) |
            (Promo.UpdateTs.cast('TEXT').like(keyword))
        ).order_by(Promo.UpdateTs.desc())
        
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
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_reward_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        rewards = Reward.select().where(
            (Reward.RewardName.cast('TEXT').like(keyword)) |
            (Reward.Points.cast('TEXT').like(keyword)) |
            (Reward.Target.cast('TEXT').like(keyword)) |
            (Reward.Description.cast('TEXT').like(keyword)) |
            (Reward.UpdateTs.cast('TEXT').like(keyword))
        ).order_by(Reward.UpdateTs.desc())
        
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
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_user_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        users = User.select().where(
            (User.OrganizationId == Organization.get_or_none(Organization.OrganizationName == entry['organizationName']).Id) &
            ((User.UserName.cast('TEXT').like(keyword)) |
            (User.AccessCode.cast('TEXT').like(keyword)) |
            (User.FullName.cast('TEXT').like(keyword)) |
            (User.BirthDate.cast('TEXT').like(keyword)) |
            (User.MobileNumber.cast('TEXT').like(keyword)) |
            (User.AccessLevel.cast('TEXT').like(keyword)) |
            (User.UpdateTs.cast('TEXT').like(keyword)))
        ).order_by(User.UpdateTs.desc())
        
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
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result