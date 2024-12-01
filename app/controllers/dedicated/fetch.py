import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import *
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
                if self.function_route == 'fetchAllOrganizationData':
                    result = self.fetchAllOrganizationData(self.entry, result)
                elif self.function_route == 'fetchMemberDataByMemberName':
                    result = self.fetchMemberDataByMemberName(self.entry, result)
                elif self.function_route == 'fetchReceiptDataByReceiptId':
                    result = self.fetchReceiptDataByReceiptId(self.entry, result)
                elif self.function_route == 'fetchAllMemberData':
                    result = self.fetchAllMemberData(self.entry, result)
                elif self.function_route == 'fetchPromoDataByPromoName':
                    result = self.fetchPromoDataByPromoName(self.entry, result)
                elif self.function_route == 'fetchAllPromoData':
                    result = self.fetchAllPromoData(self.entry, result)
                elif self.function_route == 'fetchAllItemSoldData':
                    result = self.fetchAllItemSoldData(self.entry, result)
                elif self.function_route == 'fetchAllItemRelatedData':
                    result = self.fetchAllItemRelatedData(self.entry, result)
                elif self.function_route == 'fetchAllItemPriceRelatedDataByBarcodeOrderType':
                    result = self.fetchAllItemPriceRelatedDataByBarcodeOrderType(self.entry, result)
                elif self.function_route == 'fetchAllItemPriceRelatedDataByKeywordOrderTypeInPagination':
                    result = self.fetchAllItemPriceRelatedDataByKeywordOrderTypeInPagination(self.entry, result)
                elif self.function_route == 'fetchAllStockDataByKeywordInPagination':
                    result = self.fetchAllStockDataByKeywordInPagination(self.entry, result)
                elif self.function_route == 'fetchAllItemPriceRelatedDataByKeywordInPagination':
                    result = self.fetchAllItemPriceRelatedDataByKeywordInPagination(self.entry, result)
                elif self.function_route == 'fetchAllMemberDataByKeywordInPagination':
                    result = self.fetchAllMemberDataByKeywordInPagination(self.entry, result)
                elif self.function_route == 'fetchAllPromoDataByKeywordInPagination':
                    result = self.fetchAllPromoDataByKeywordInPagination(self.entry, result)
                elif self.function_route == 'fetchAllRewardDataByKeywordInPagination':
                    result = self.fetchAllRewardDataByKeywordInPagination(self.entry, result)
                elif self.function_route == 'fetchAllUserDataByKeywordInPagination':
                    result = self.fetchAllUserDataByKeywordInPagination(self.entry, result)
                elif self.function_route == 'fetchAllReceiptDataByKeywordInPagination':
                    result = self.fetchAllReceiptDataByKeywordInPagination(self.entry, result)
                elif self.function_route == 'fetchAllItemDataByKeywordInPagination':
                    result = self.fetchAllItemDataByKeywordInPagination(self.entry, result)
                elif self.function_route == 'fetchAllBrandDataByKeywordInPagination':
                    result = self.fetchAllBrandDataByKeywordInPagination(self.entry, result)
                elif self.function_route == 'fetchAllItemTypeDataByKeywordInPagination':
                    result = self.fetchAllItemTypeDataByKeywordInPagination(self.entry, result)
                elif self.function_route == 'fetchAllSupplierDataByKeywordInPagination':
                    result = self.fetchAllSupplierDataByKeywordInPagination(self.entry, result)
                
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
        print(f"{self.function_route} -> result_message: {result['message']}")

    # add function here
    def fetchAllOrganizationData(self, entry=None, result=None):
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
                    'password': organization.Password,
                })
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

    def fetchPromoDataByPromoName(self, entry=None, result=None):
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

    def fetchMemberDataByMemberName(self, entry=None, result=None):
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

    def fetchReceiptDataByReceiptId(self, entry=None, result=None):
        try:
            receipt = Receipt.select().where(Receipt.Id == entry['receiptId'])
            
            if not receipt.exists():
                result['message'] = 'Receipt does not exists'
                return result
            
            receipt = receipt.first()
            
            result['success'] = True
            result['dictData'] = {
                'organizationId': receipt.OrganizationId,
                'userId': receipt.UserId,
                'memberId': receipt.MemberId,
                'memberName': Member.get_or_none(Member.Id == receipt.MemberId).MemberName if receipt.MemberId else None,
                'mobileNumber': Member.get_or_none(Member.Id == receipt.MemberId).MobileNumber if receipt.MemberId else None,
                'dateId': receipt.DateId,
                'orderTypeId': receipt.OrderTypeId,
                'referenceId': receipt.ReferenceId,
                'orderName': receipt.OrderName,
                'billing': receipt.Billing,
            }

            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

    def fetchAllPromoData(self, entry=None, result=None):
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
        
    def fetchAllItemSoldData(self, entry=None, result=None):
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
                    'itemName': Item.get_or_none(Item.Id == itemSold.ItemId).ItemName if itemSold.ItemId else None,
                    'quantity': itemSold.Quantity,
                    'total': itemSold.Total,
                    'voidReason': itemSold.VoidReason,
                    'status': itemSold.VoidStatus,
                    'stockBypass': itemSold.StockBypass,
                    'updateTs': itemSold.UpdateTs,
                })
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
    
    def fetchAllMemberData(self, entry=None, result=None):
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
        
        
    def fetchAllItemRelatedData(self, entry=None, result=None):
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
        
    def fetchAllItemPriceRelatedDataByBarcodeOrderType(self, entry=None, result=None):
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
            
            existingItemId = []
            
            result['success'] = True
            
            for itemPrice in itemPrices:
                item = itemPrice.ItemId
                brand = item.BrandId
                salesGroup = item.SalesGroupId
                promo = itemPrice.PromoId
                stock = Stock.get_or_none(Stock.ItemId == item.Id)
                
                if itemPrice.EffectiveDate > datetime.now().date():
                    continue
                
                if item.Id in existingItemId:
                    continue
                
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
                
                existingItemId.append(item.Id)
                
            return result
        
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
        
    def fetchAllItemPriceRelatedDataByKeywordOrderTypeInPagination(self, entry=None, result=None):
        try:
            limit = 15
            offset = (entry['currentPage'] - 1) * limit
            keyword = f"%{entry['keyword']}%"
            orderType = entry['orderType']
            
            itemPrices = None
        
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
            
            if itemPrices is None:
                result['message'] = f"Invalid order type: {orderType}"
                return result
            
            totalCount = itemPrices.count()
            paginatedItemPrices = itemPrices.limit(limit).offset(offset)
            existingItemId = []
            
            result['success'] = True
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
            for itemPrice in paginatedItemPrices:
                item = itemPrice.ItemId
                brand = item.BrandId
                salesGroup = item.SalesGroupId
                promo = itemPrice.PromoId
                stock = Stock.get_or_none(Stock.ItemId == item.Id)
                
                # TODO: fix filtering should exclude duplicate 
                if itemPrice.EffectiveDate > datetime.now().date():
                    continue
                
                if item.Id in existingItemId:
                    continue
                
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
                existingItemId.append(item.Id)
                
            return result
        
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

    def fetchAllItemPriceRelatedDataByKeywordInPagination(self, entry=None, result=None):
        try:
            limit = 15
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
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
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
                    'cost': itemPrice.Cost,
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

    def fetchAllStockDataByKeywordInPagination(self, entry=None, result=None):
        try:
            limit = 15
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
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
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
        
    def fetchAllMemberDataByKeywordInPagination(self, entry=None, result=None):
        try:
            limit = 15
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
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
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
        
    def fetchAllPromoDataByKeywordInPagination(self, entry=None, result=None):
        try:
            limit = 15
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
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
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
        
    def fetchAllItemDataByKeywordInPagination(self, entry=None, result=None):
        try:
            limit = 15
            offset = (entry['currentPage'] - 1) * limit
            keyword = f"%{entry['keyword']}%"
        
            items = Item.select(
                Item,
                ItemType,
                Brand,
                Supplier,
                SalesGroup,
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
                (Item.UpdateTs.cast('TEXT').like(keyword))
            ).order_by(Item.UpdateTs.desc())
            
            totalCount = items.count()
            paginatedItems = items.limit(limit).offset(offset)
            
            result['success'] = True
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
            for item in paginatedItems:
                itemType = item.ItemTypeId
                brand = item.BrandId
                supplier = item.SupplierId
                salesGroup = item.SalesGroupId
                
                result['listData'].append({
                    'id': item.Id,
                    'itemName': item.ItemName,
                    'barcode': item.Barcode,
                    'expireDate': item.ExpireDate,
                    'itemTypeName': itemType.ItemTypeName,
                    'brandName': brand.BrandName,
                    'supplierName': supplier.SupplierName,
                    'salesGroupName': salesGroup.SalesGroupName,
                    'updateTs': item.UpdateTs,
                })
            
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
                
    def fetchAllBrandDataByKeywordInPagination(self, entry=None, result=None):
        try:
            limit = 15
            offset = (entry['currentPage'] - 1) * limit
            keyword = f"%{entry['keyword']}%"
            
            brands = Brand.select().where(
                (Brand.BrandName.cast('TEXT').like(keyword)) |
                (Brand.UpdateTs.cast('TEXT').like(keyword))
            ).order_by(Brand.UpdateTs.desc())
            
            totalCount = brands.count()
            paginatedBrands = brands.limit(limit).offset(offset)
            
            result['success'] = True
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
            for brand in paginatedBrands:
                result['listData'].append({
                    'id': brand.Id,
                    'brandName': brand.BrandName,
                    'updateTs': brand.UpdateTs,
                })
            
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def fetchAllItemTypeDataByKeywordInPagination(self, entry=None, result=None):
        try:
            limit = 15
            offset = (entry['currentPage'] - 1) * limit
            keyword = f"%{entry['keyword']}%"
            
            itemTypes = ItemType.select().where(
                (ItemType.ItemTypeName.cast('TEXT').like(keyword)) |
                (ItemType.UpdateTs.cast('TEXT').like(keyword))
            ).order_by(ItemType.UpdateTs.desc())
            
            totalCount = itemTypes.count()
            paginatedItemTypes = itemTypes.limit(limit).offset(offset)
            
            result['success'] = True
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
            for itemType in paginatedItemTypes:
                result['listData'].append({
                    'id': itemType.Id,
                    'itemTypeName': itemType.ItemTypeName,
                    'updateTs': itemType.UpdateTs,
                })
            
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def fetchAllSupplierDataByKeywordInPagination(self, entry=None, result=None):
        try:
            limit = 15
            offset = (entry['currentPage'] - 1) * limit
            keyword = f"%{entry['keyword']}%"
            
            suppliers = Supplier.select().where(
                (Supplier.SupplierName.cast('TEXT').like(keyword)) |
                (Supplier.UpdateTs.cast('TEXT').like(keyword))
            ).order_by(Supplier.UpdateTs.desc())
            
            totalCount = suppliers.count()
            paginatedSuppliers = suppliers.limit(limit).offset(offset)
            
            result['success'] = True
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
            for supplier in paginatedSuppliers:
                result['listData'].append({
                    'id': supplier.Id,
                    'supplierName': supplier.SupplierName,
                    'updateTs': supplier.UpdateTs,
                })
            
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def fetchAllRewardDataByKeywordInPagination(self, entry=None, result=None):
        try:
            limit = 15
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
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
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
        
    def fetchAllUserDataByKeywordInPagination(self, entry=None, result=None):
        try:
            limit = 15
            offset = (entry['currentPage'] - 1) * limit
            keyword = f"%{entry['keyword']}%"
            
            users = User.select().where(
                ((User.OrganizationId == Organization.get_or_none(Organization.OrganizationName == entry['organizationName']).Id) &
                (User.AccessLevel < 3)) &
                ((User.UserName.cast('TEXT').like(keyword)) |
                (User.Password.cast('TEXT').like(keyword)) |
                (User.FullName.cast('TEXT').like(keyword)) |
                (User.BirthDate.cast('TEXT').like(keyword)) |
                (User.MobileNumber.cast('TEXT').like(keyword)) |
                (User.AccessLevel.cast('TEXT').like(keyword)) |
                (User.UpdateTs.cast('TEXT').like(keyword)))
            ).order_by(User.UpdateTs.desc())
            
            totalCount = users.count()
            paginatedUsers = users.limit(limit).offset(offset)
            
            result['success'] = True
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
            for user in paginatedUsers:
                result['listData'].append({
                    'id': user.Id,
                    'userName': user.UserName,
                    'password': user.Password,
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

    def fetchAllReceiptDataByKeywordInPagination(self, entry=None, result=None):
        try:
            limit = 15
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
                (Receipt.ReferenceId.cast('TEXT').like(keyword)) |
                (Receipt.MachineId.cast('TEXT').like(keyword)) |
                (Receipt.OrderName.cast('TEXT').like(keyword)) |
                (Receipt.UpdateTs.cast('TEXT').like(keyword)))
            ).order_by(Receipt.UpdateTs.desc())
            
            totalCount = receipts.count()
            paginatedReceipts = receipts.limit(limit).offset(offset)
            
            result['success'] = True
            result['dictData'] = {'totalPages': 1 if totalCount == 0 else math.ceil(totalCount / limit)}
            for receipt in paginatedReceipts:
                organization = receipt.OrganizationId
                user = receipt.UserId
                member = receipt.MemberId
                date = receipt.DateId
                orderType = receipt.OrderTypeId
            
                result['listData'].append({
                    'id': receipt.Id,
                    'organizationId': receipt.OrganizationId,
                    'userId': receipt.UserId,
                    'memberId': receipt.MemberId, 
                    'organizationName': organization.OrganizationName,
                    'userName': user.UserName,
                    'memberName': member.MemberName if member else None, # TODO: check the other queries/controllers if some of it have the same case
                    'dateValue': date.DateValue,
                    'orderTypeName': orderType.OrderTypeName,
                    'referenceId': receipt.ReferenceId,
                    'machineId': receipt.MachineId,
                    'orderName': receipt.OrderName,
                    'billing': receipt.Billing,
                    'updateTs': receipt.UpdateTs,
                })
            
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

    
    
    
