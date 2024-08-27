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
    Receipt,
    Date,
    OrderType,
    ItemSold,
    Reason,
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
                elif self.function_route == 'fetch_member_data_by_member_name':
                    result = fetch_member_data_by_member_name(self.entry, result)
                elif self.function_route == 'fetch_all_member_data':
                    result = fetch_all_member_data(self.entry, result)
                elif self.function_route == 'fetch_promo_data_by_promo_name':
                    result = fetch_promo_data_by_promo_name(self.entry, result)
                elif self.function_route == 'fetch_all_promo_data':
                    result = fetch_all_promo_data(self.entry, result)
                elif self.function_route == 'fetch_all_reason_data':
                    result = fetch_all_reason_data(self.entry, result)
                elif self.function_route == 'fetch_all_item_sold_data':
                    result = fetch_all_item_sold_data(self.entry, result)
                elif self.function_route == 'fetch_all_item_related_data':
                    result = fetch_all_item_related_data(self.entry, result)
                elif self.function_route == 'fetch_all_item_price_related_data_by_barcode_order_type':
                    result = fetch_all_item_price_related_data_by_barcode_order_type(self.entry, result)
                elif self.function_route == 'fetch_all_item_price_related_data_by_keyword_order_type_in_pagination':
                    result = fetch_all_item_price_related_data_by_keyword_order_type_in_pagination(self.entry, result)
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
                elif self.function_route == 'fetch_all_receipt_data_by_keyword_in_pagination':
                    result = fetch_all_receipt_data_by_keyword_in_pagination(self.entry, result)
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

def fetch_member_data_by_member_name(entry=None, result=None):
    try:
        member = Member.select().where(Member.MemberName == entry['memberName']).order_by(Member.UpdateTs.desc())
        
        if not member.exists():
            result['message'] = 'Member does not exists'
            return result
        
        member = member.first()
        organization = member.OrganizationId
        
        result['success'] = True
        result['dictData'] = {
            'id': member.Id,
            'organizationId': organization.Id,
            'memberName': member.MemberName,
            'birthDate': member.BirthDate,
            'address': member.Address,
            'mobileNumber': member.MobileNumber,
            'points': member.Points,
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
    
def fetch_all_reason_data(entry=None, result=None):
    try:
        reasons = Reason.select().order_by(Reason.UpdateTs.desc())
        
        if not reasons.exists():
            result['message'] = 'Reason does not exists'
            return result
        
        result['success'] = True
        for reason in reasons:
            result['listData'].append({
                'id': reason.Id,
                'reasonName': reason.ReasonName,
                'updateTs': reason.UpdateTs,
            })
        return result

    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
 
    
def fetch_all_item_sold_data(entry=None, result=None):
    try:
        itemSolds = ItemSold.select().where(ItemSold.ReceiptId == entry['receiptId']).order_by(ItemSold.UpdateTs.desc())
        
        if not itemSolds.exists():
            result['message'] = 'ItemSold does not exists'
            return result
        
        result['success'] = True
        for itemSold in itemSolds:
            result['listData'].append({
                'id': itemSold.Id,
                'receiptId': itemSold.ReceiptId,
                'itemId': itemSold.ItemId,
                'itemName': Item.get_or_none(Item.Id == itemSold.ItemId).ItemName,
                'quantity': itemSold.Quantity,
                'total': itemSold.Total,
                'reasonId': itemSold.ReasonId,
                'status': itemSold.Status,
                'updateTs': itemSold.UpdateTs,
            })
        return result

    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
   
def fetch_all_member_data(entry=None, result=None):
    try:
        members = Member.select().order_by(Member.UpdateTs.desc())
        
        if not members.exists():
            result['message'] = 'Member does not exists'
            return result
        
        result['success'] = True
        for member in members:
            result['listData'].append({
                'id': member.Id,
                'organizationName': Organization.get_or_none(Organization.Id == member.OrganizationId).OrganizationName,
                'memberName': member.MemberName,
                'birthDate': member.BirthDate,
                'address': member.Address,
                'mobileNumber': member.MobileNumber,
                'points': member.Points,
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
    
def fetch_all_item_price_related_data_by_barcode_order_type(entry=None, result=None):
    try:
        barcode = entry['barcode']
        orderType = entry['orderType']
        
        if orderType == 'MIXED':
            itemPrices = (ItemPrice.select(
                ItemPrice,
                Item,
                Promo,
                Brand,
                SalesGroup,
            ).join(Item, JOIN.LEFT_OUTER, on=(ItemPrice.ItemId == Item.Id)
            ).join(Promo, JOIN.LEFT_OUTER, on=(ItemPrice.PromoId == Promo.Id)
            ).join(Brand, JOIN.LEFT_OUTER, on=(Item.BrandId == Brand.Id)
            ).join(SalesGroup, JOIN.LEFT_OUTER, on=(Item.SalesGroupId == SalesGroup.Id)
            ).where(
                (Item.Barcode == barcode)
            ).order_by(ItemPrice.UpdateTs.desc(), ItemPrice.EffectiveDate.desc()))
        
        else:
            itemPrices = (ItemPrice.select(
                ItemPrice,
                Item,
                Promo,
                Brand,
                SalesGroup,
            ).join(Item, JOIN.LEFT_OUTER, on=(ItemPrice.ItemId == Item.Id)
            ).join(Promo, JOIN.LEFT_OUTER, on=(ItemPrice.PromoId == Promo.Id)
            ).join(Brand, JOIN.LEFT_OUTER, on=(Item.BrandId == Brand.Id)
            ).join(SalesGroup, JOIN.LEFT_OUTER, on=(Item.SalesGroupId == SalesGroup.Id)
            ).where(
                (SalesGroup.SalesGroupName == orderType) &
                (Item.Barcode == barcode)
            ).order_by(ItemPrice.UpdateTs.desc(), ItemPrice.EffectiveDate.desc()))
        
        result['success'] = True
        for itemPrice in itemPrices:
            item = itemPrice.ItemId
            brand = item.BrandId
            salesGroup = item.SalesGroupId
            promo = itemPrice.PromoId
            stock = Stock.get_or_none(Stock.ItemId == item.Id)
            
            if itemPrice.EffectiveDate < datetime.now().date():
                # TODO: write a filter logic here where
                result['listData'].append({
                    # ids for editting purpose
                    'itemId': item.Id,
                    'brandId': brand.Id,
                    'salesGroupId': salesGroup.Id,
                    'itemPriceId': itemPrice.Id,
                    'promoId': promo.Id if promo else None,
                    'stockId': stock.Id if stock else None,
                    # ids for displaying purpose
                    'itemName': item.ItemName,
                    'barcode': item.Barcode,
                    'brandName': brand.BrandName,
                    'price': itemPrice.Price,
                    'discount': itemPrice.Discount,
                    'promoName': promo.PromoName if promo else None,
                    'available': stock.Available if stock else None,
                    'updateTs': itemPrice.UpdateTs,
                })
            
        return result
    
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def fetch_all_item_price_related_data_by_keyword_order_type_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        orderType = entry['orderType']
    
        if orderType == 'RETAIL' or orderType == 'WHOLESALE':
            itemPrices = (ItemPrice.select(
                ItemPrice,
                Item,
                Promo,
                Brand,
                SalesGroup,
            ).join(Item, JOIN.LEFT_OUTER, on=(ItemPrice.ItemId == Item.Id)
            ).join(Promo, JOIN.LEFT_OUTER, on=(ItemPrice.PromoId == Promo.Id)
            ).join(Brand, JOIN.LEFT_OUTER, on=(Item.BrandId == Brand.Id)
            ).join(SalesGroup, JOIN.LEFT_OUTER, on=(Item.SalesGroupId == SalesGroup.Id)
            ).where(
                (SalesGroup.SalesGroupName == orderType) &
                ((Item.ItemName.cast('TEXT').like(keyword)) |
                (Item.Barcode.cast('TEXT').like(keyword)) |
                (Brand.BrandName.cast('TEXT').like(keyword)) |
                (ItemPrice.EffectiveDate.cast('TEXT').like(keyword)) |
                (Promo.PromoName.cast('TEXT').like(keyword)) |
                (ItemPrice.UpdateTs.cast('TEXT').like(keyword)))
            ).order_by(ItemPrice.UpdateTs.desc(), ItemPrice.EffectiveDate.desc()))
        
        if orderType == 'MIXED':
            itemPrices = (ItemPrice.select(
                ItemPrice,
                Item,
                Promo,
                Brand,
                SalesGroup,
            ).join(Item, JOIN.LEFT_OUTER, on=(ItemPrice.ItemId == Item.Id)
            ).join(Promo, JOIN.LEFT_OUTER, on=(ItemPrice.PromoId == Promo.Id)
            ).join(Brand, JOIN.LEFT_OUTER, on=(Item.BrandId == Brand.Id)
            ).join(SalesGroup, JOIN.LEFT_OUTER, on=(Item.SalesGroupId == SalesGroup.Id)
            ).where(
                (Item.ItemName.cast('TEXT').like(keyword)) |
                (Item.Barcode.cast('TEXT').like(keyword)) |
                (Brand.BrandName.cast('TEXT').like(keyword)) |
                (ItemPrice.EffectiveDate.cast('TEXT').like(keyword)) |
                (Promo.PromoName.cast('TEXT').like(keyword)) |
                (ItemPrice.UpdateTs.cast('TEXT').like(keyword))
            ).order_by(ItemPrice.UpdateTs.desc(), ItemPrice.EffectiveDate.desc()))
        
        totalCount = itemPrices.count()
        paginatedItemPrices = itemPrices.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(totalCount / limit) if 0 else 1}
        for itemPrice in paginatedItemPrices:
            item = itemPrice.ItemId
            brand = item.BrandId
            salesGroup = item.SalesGroupId
            promo = itemPrice.PromoId
            stock = Stock.get_or_none(Stock.ItemId == item.Id)
            
            if itemPrice.EffectiveDate < datetime.now().date():
                # TODO: write a filter logic here where
                result['listData'].append({
                    # ids for editting purpose
                    'itemId': item.Id,
                    'brandId': brand.Id,
                    'salesGroupId': salesGroup.Id,
                    'itemPriceId': itemPrice.Id,
                    'promoId': promo.Id if promo else None,
                    'stockId': stock.Id if stock else None,
                    # ids for displaying purpose
                    'itemName': item.ItemName,
                    'barcode': item.Barcode,
                    'brandName': brand.BrandName,
                    'price': itemPrice.Price,
                    'discount': itemPrice.Discount,
                    'promoName': promo.PromoName if promo else None,
                    'available': stock.Available if stock else None,
                    'updateTs': itemPrice.UpdateTs,
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
        
        totalCount = stocks.count()
        paginatedStocks = stocks.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(totalCount / limit) if 0 else 1}
        for stocks in paginatedStocks:
            result['listData'].append({
                'id': stocks.Id,
                'itemName': stocks.ItemId.ItemName,
                'salesGroupName': stocks.ItemId.SalesGroupId.SalesGroupName,
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
        
        itemPrices = (ItemPrice.select(
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
        
        totalCount = itemPrices.count()
        paginatedItemPrices = itemPrices.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(totalCount / limit) if 0 else 1}
        for itemPrice in paginatedItemPrices:
            item = itemPrice.ItemId
            itemType = item.ItemTypeId
            brand = item.BrandId
            supplier = item.SupplierId
            salesGroup = item.SalesGroupId
            promo = itemPrice.PromoId
            stock = Stock.get_or_none(Stock.ItemId == item.Id)
            
            result['listData'].append({
                # ids for editting purpose
                'itemId': item.Id,
                'itemTypeId': itemType.Id,
                'brandId': brand.Id,
                'supplierId': supplier.Id,
                'salesGroupId': salesGroup.Id,
                'itemPriceId': itemPrice.Id,
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
                'capital': itemPrice.Capital,
                'price': itemPrice.Price,
                'discount': itemPrice.Discount,
                'effectiveDate': itemPrice.EffectiveDate,
                'promoName': promo.PromoName if promo else None,
                'updateTs': itemPrice.UpdateTs,
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
        
        totalCount = members.count()
        paginatedMembers = members.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(totalCount / limit) if 0 else 1}
        for member in paginatedMembers:
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
        
        totalCount = promos.count()
        paginatedPromos = promos.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(totalCount / limit) if 0 else 1}
        for promo in paginatedPromos:
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
        
        totalCount = rewards.count()
        paginatedRewards = rewards.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(totalCount / limit) if 0 else 1}
        for reward in paginatedRewards:
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
            ((User.OrganizationId == Organization.get_or_none(Organization.OrganizationName == entry['organizationName']).Id) &
            (User.AccessLevel < 3)) &
            ((User.UserName.cast('TEXT').like(keyword)) |
            (User.AccessCode.cast('TEXT').like(keyword)) |
            (User.FullName.cast('TEXT').like(keyword)) |
            (User.BirthDate.cast('TEXT').like(keyword)) |
            (User.MobileNumber.cast('TEXT').like(keyword)) |
            (User.AccessLevel.cast('TEXT').like(keyword)) |
            (User.UpdateTs.cast('TEXT').like(keyword)))
        ).order_by(User.UpdateTs.desc())
        
        totalCount = users.count()
        paginatedUsers = users.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(totalCount / limit) if 0 else 1}
        for user in paginatedUsers:
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

def fetch_all_receipt_data_by_keyword_in_pagination(entry=None, result=None):
    try:
        limit = 30
        offset = (entry['currentPage'] - 1) * limit
        keyword = f"%{entry['keyword']}%"
        
        receipts = Receipt.select(
            Receipt, 
            User, 
            Member, 
            Date,
            OrderType
        ).join(User, JOIN.LEFT_OUTER, on=(Receipt.UserId == User.Id)
        ).join(Member, JOIN.LEFT_OUTER, on=(Receipt.MemberId == Member.Id)
        ).join(Date, JOIN.LEFT_OUTER, on=(Receipt.DateId == Date.Id)
        ).join(OrderType, JOIN.LEFT_OUTER, on=(Receipt.OrderTypeId == OrderType.Id)
        ).where(
            (Receipt.OrganizationId == Organization.get_or_none(Organization.OrganizationName == entry['organizationName']).Id) &
            ((User.UserName.cast('TEXT').like(keyword)) |
            (Member.MemberName.cast('TEXT').like(keyword)) |
            (Date.DateValue.cast('TEXT').like(keyword)) |
            (OrderType.OrderTypeName.cast('TEXT').like(keyword)) |
            (Receipt.OrderName.cast('TEXT').like(keyword)) |
            (Receipt.UpdateTs.cast('TEXT').like(keyword)))
        ).order_by(Receipt.UpdateTs.desc())
        
        totalCount = receipts.count()
        paginatedReceipts = receipts.limit(limit).offset(offset)
        
        result['success'] = True
        result['dictData'] = {'totalPages': math.ceil(totalCount / limit) if 0 else 1}
        for receipt in paginatedReceipts:
            organization = receipt.OrganizationId
            user = receipt.UserId
            member = receipt.MemberId
            date = receipt.DateId
            orderType = receipt.OrderTypeId
        
            result['listData'].append({
                'id': receipt.Id,
                'organizationName': organization.OrganizationName,
                'userName': user.UserName,
                'memberName': member.MemberName,
                'dateValue': date.DateValue,
                'orderTypeName': orderType.OrderTypeName,
                'referenceId': receipt.ReferenceId,
                'orderName': receipt.OrderName,
                'orderSummary': receipt.OrderSummary,
                'orderPayment': receipt.OrderPayment,
                'updateTs': receipt.UpdateTs,
            })
        
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result

    
    
    
