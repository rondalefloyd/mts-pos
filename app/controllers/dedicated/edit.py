import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import *
from app.utils.databases import postgres_db


class EditThread(QThread):
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
                if self.function_route == 'editProductRelatedDataById':
                    result = self.editProductRelatedDataById(self.entry, result)
                elif self.function_route == 'editMemberDataById':
                    result = self.editMemberDataById(self.entry, result)
                elif self.function_route == 'editPromoDataById':
                    result = self.editPromoDataById(self.entry, result)
                elif self.function_route == 'editItemTypeDataById':
                    result = self.editItemTypeDataById(self.entry, result)
                elif self.function_route == 'editBrandDataById':
                    result = self.editBrandDataById(self.entry, result)
                elif self.function_route == 'editSupplierDataById':
                    result = self.editSupplierDataById(self.entry, result)
                elif self.function_route == 'editItemDataById':
                    result = self.editItemDataById(self.entry, result)
                elif self.function_route == 'editRewardDataById':
                    result = self.editRewardDataById(self.entry, result)
                elif self.function_route == 'editStockDataById':
                    result = self.editStockDataById(self.entry, result)
                elif self.function_route == 'editOrganizationDataById':
                    result = self.editOrganizationDataById(self.entry, result)
                elif self.function_route == 'editUserDataById':
                    result = self.editUserDataById(self.entry, result)
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
        
    def editProductRelatedDataById(self, entry=None, result=None):
        try:
            entry['itemName'] = entry['itemName'] if entry['itemName'] != '' else '-'
            entry['barcode'] = entry['barcode'] if entry['barcode'] != '' else '-'
            entry['itemTypeName'] = entry['itemTypeName'] if entry['itemTypeName'] != '' else '-'
            entry['brandName'] = entry['brandName'] if entry['brandName'] != '' else '-'
            entry['supplierName'] = entry['supplierName'] if entry['supplierName'] != '' else '-'
            entry['salesGroupName'] = entry['salesGroupName'] if entry['salesGroupName'] != '' else '-'
            entry['cost'] = entry['cost'] if entry['cost'] != '' else '0'
            entry['price'] = entry['price'] if entry['price'] != '' else '0'
            
            itemType = ItemType.select().where(ItemType.ItemTypeName == entry['itemTypeName'])
            brand = Brand.select().where(Brand.BrandName == entry['brandName'])
            supplier = Supplier.select().where(Supplier.SupplierName == entry['supplierName'])
            salesGroup = SalesGroup.select().where(SalesGroup.SalesGroupName == entry['salesGroupName'])
            
            itemType = ItemType.create(ItemTypeName=entry['itemTypeName']) if not itemType.exists() else itemType.first()
            brand = Brand.create(BrandName=entry['brandName']) if not brand.exists() else brand.first()
            supplier = Supplier.create(SupplierName=entry['supplierName']) if not supplier.exists() else supplier.first()
            salesGroup = SalesGroup.create(SalesGroupName=entry['salesGroupName']) if not salesGroup.exists() else salesGroup.first()
            
            item = Item.select().where(
                (Item.ItemName == entry['itemName']) &
                (Item.SalesGroupId == SalesGroup.get(SalesGroup.SalesGroupName == entry['salesGroupName']).Id)
            )
            
            item = Item.create(
                ItemName=entry['itemName'],
                Barcode=entry['barcode'],
                ExpireDate=entry['expireDate'],
                ItemTypeId=itemType.Id,
                BrandId=brand.Id,
                SupplierId=supplier.Id,
                SalesGroupId=salesGroup.Id,
            ) if not item.exists() else item.first()

            if entry['applyPromo'] is True and entry['promoId'] is None:
                itemPrice = ItemPrice.get_or_none(ItemPrice.Id == entry['itemPriceId'])
                itemPrice.ItemId = item.Id
                itemPrice.Cost = entry['cost']
                itemPrice.Price = entry['price']
                itemPrice.EffectiveDate = datetime.strptime(entry['endDate'], '%Y-%m-%d')
                itemPrice.UpdateTs = datetime.now()
                itemPrice.save()
                
                itemPrice = ItemPrice.select().where(
                    (ItemPrice.ItemId == item.Id) &
                    (ItemPrice.Price == entry['newPrice']) & 
                    (ItemPrice.PromoId == Promo.get_or_none(Promo.PromoName == entry['promoName']).Id) & 
                    (ItemPrice.EffectiveDate == datetime.strptime(entry['startDate'], '%Y-%m-%d')) 
                )
                
                if itemPrice.exists():
                    result['message'] = 'ItemPrice already exists'
                    return result
                
                itemPrice = ItemPrice.create(
                    ItemId=item.Id,
                    Cost=entry['cost'],
                    Price=entry['newPrice'],
                    PromoId=Promo.get_or_none(Promo.PromoName == entry['promoName']).Id,
                    Discount=entry['discount'],
                    EffectiveDate=entry['startDate'],
                )
                
            elif entry['applyPromo'] is False and entry['promoId'] is None:
                itemPrice = ItemPrice.select().where(
                    (ItemPrice.ItemId == item.Id) &
                    (ItemPrice.Price == entry['price']) & 
                    (ItemPrice.EffectiveDate == entry['effectiveDate']) 
                )
                
                itemPrice = itemPrice.first()
                itemPrice.ItemId = item.Id
                itemPrice.Cost = entry['cost']
                itemPrice.Price = entry['price']
                itemPrice.EffectiveDate = entry['effectiveDate']
                itemPrice.save()
                
            if entry['trackInventory'] is True and entry['stockId'] is None:
                stock = Stock.create(ItemId=item.Id)
                
            result['success'] = True
            result['message'] = 'ItemPrice updated'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def editMemberDataById(self, entry=None, result=None):
        try:
            entry['memberName'] = entry['memberName'] if entry['memberName'] != '' else '-'
            entry['address'] = entry['address'] if entry['address'] != '' else '-'
            entry['mobileNumber'] = entry['mobileNumber'] if entry['mobileNumber'] != '' else '-'
            entry['points'] = entry['points'] if entry['points'] != '' else '0'
            
            member = Member.get_or_none(Member.Id == entry['id'])
            member.MemberName = entry['memberName']
            member.BirthDate = entry['birthDate']
            member.Address = entry['address']
            member.MobileNumber = entry['mobileNumber']
            member.Points = entry['points']
            member.UpdateTs = datetime.now()
            member.save()
            
            result['success'] = True
            result['message'] = 'Member updated'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def editPromoDataById(self, entry=None, result=None):
        try:
            entry['promoName'] = entry['promoName'] if entry['promoName'] != '' else '-'
            entry['discountRate'] = entry['discountRate'] if entry['discountRate'] != '' else '0'
            entry['description'] = entry['description'] if entry['description'] != '' else '-'
            
            promo = Promo.get_or_none(Promo.Id == entry['id'])
            promo.PromoName = entry['promoName']
            promo.DiscountRate = entry['discountRate']
            promo.Description = entry['description']
            promo.UpdateTs = datetime.now()
            promo.save()
            
            result['success'] = True
            result['message'] = 'Promo updated'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
                
    def editItemTypeDataById(self, entry=None, result=None):
        try:
            entry['itemTypeName'] = entry['itemTypeName'] if entry['itemTypeName'] != '' else '-'
            
            itemType = ItemType.get_or_none(ItemType.Id == entry['id'])
            itemType.ItemTypeName = entry['itemTypeName']
            itemType.UpdateTs = datetime.now()
            itemType.save()
            
            result['success'] = True
            result['message'] = 'ItemType updated'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
                
    def editBrandDataById(self, entry=None, result=None):
        try:
            entry['brandName'] = entry['brandName'] if entry['brandName'] != '' else '-'
            
            brand = Brand.get_or_none(Brand.Id == entry['id'])
            brand.BrandName = entry['brandName']
            brand.UpdateTs = datetime.now()
            brand.save()
            
            result['success'] = True
            result['message'] = 'Brand updated'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
                
    def editSupplierDataById(self, entry=None, result=None):
        try:
            entry['supplierName'] = entry['supplierName'] if entry['supplierName'] != '' else '-'
            
            supplier = Supplier.get_or_none(Supplier.Id == entry['id'])
            supplier.SupplierName = entry['supplierName']
            supplier.UpdateTs = datetime.now()
            supplier.save()
            
            result['success'] = True
            result['message'] = 'Supplier updated'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
                
    def editItemDataById(self, entry=None, result=None):
        try:
            entry['itemName'] = entry['itemName'] if entry['itemName'] != '' else '-'
            entry['barcode'] = entry['barcode'] if entry['barcode'] != '' else '-'
            entry['itemTypeName'] = entry['itemTypeName'] if entry['itemTypeName'] != '' else '-'
            entry['brandName'] = entry['brandName'] if entry['brandName'] != '' else '-'
            entry['supplierName'] = entry['supplierName'] if entry['supplierName'] != '' else '-'
            
            item = Item.get_or_none(Item.Id == entry['id'])
            item.ItemName = entry['itemName']
            item.Barcode = entry['barcode']
            item.ExpireDate = entry['expireDate']
            item.ItemTypeId = ItemType.get(ItemType.ItemTypeName == entry['itemTypeName']).Id
            item.BrandId = Brand.get(Brand.BrandName == entry['brandName']).Id
            item.SupplierId = Supplier.get(Supplier.SupplierName == entry['supplierName']).Id
            item.UpdateTs = datetime.now()
            item.save()
            
            result['success'] = True
            result['message'] = 'Item updated'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def editRewardDataById(self, entry=None, result=None):
        try:
            entry['rewardName'] = entry['rewardName'] if entry['rewardName'] != '' else '-'
            entry['points'] = entry['points'] if entry['points'] != '' else '0'
            entry['target'] = entry['target'] if entry['target'] != '' else '0'
            entry['description'] = entry['description'] if entry['description'] != '' else '-'
            
            reward = Reward.get_or_none(Reward.Id == entry['id'])
            reward.RewardName = entry['rewardName']
            reward.Points = entry['points']
            reward.Target = entry['target']
            reward.Description = entry['description']
            reward.UpdateTs = datetime.now()
            reward.save()
            
            result['success'] = True
            result['message'] = 'Reward updated'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

    def editStockDataById(self, entry=None, result=None):
        try:
            entry['onHand'] = entry['onHand'] if entry['onHand'] != '' else '0'
            entry['available'] = entry['available'] if entry['available'] != '' else '0'
            
            stock = Stock.get_or_none(Stock.Id == entry['id'])
            stock.OnHand = entry['onHand']
            stock.Available = entry['available']
            stock.UpdateTs = datetime.now()
            stock.save()
            
            result['success'] = True
            result['message'] = 'Stock updated'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

    def editOrganizationDataById(self, entry=None, result=None):
        try:
            entry['taxId'] = entry['taxId'] if entry['taxId'] != '' else '-'
            entry['organizationName'] = entry['organizationName'] if entry['organizationName'] != '' else '-'
            entry['address'] = entry['address'] if entry['address'] != '' else '-'
            entry['mobileNumber'] = entry['mobileNumber'] if entry['mobileNumber'] != '' else '-'
            
            organization = Organization.get_or_none(Organization.Id == entry['id'])
            organization.TaxId = entry['taxId']
            organization.OrganizationName = entry['organizationName']
            organization.Address = entry['address']
            organization.MobileNumber = entry['mobileNumber']
            organization.Password = entry['password']
            organization.UpdateTs = datetime.now()
            organization.save()
            
            result['success'] = True
            result['message'] = 'Organization updated'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def editUserDataById(self, entry=None, result=None):
        try:
            entry['userName'] = entry['userName'] if entry['userName'] != '' else '-'
            entry['fullName'] = entry['fullName'] if entry['fullName'] != '' else '-'
            entry['mobileNumber'] = entry['mobileNumber'] if entry['mobileNumber'] != '' else '-'
            
            user = User.get_or_none(User.Id == entry['id'])
            user.UserName = entry['userName']
            user.Password = entry['password']
            user.FullName = entry['fullName']
            user.BirthDate = entry['birthDate']
            user.MobileNumber = entry['mobileNumber']
            user.AccessLevel = entry['accessLevel']
            user.UpdateTs = datetime.now()
            user.save()
            
            result['success'] = True
            result['message'] = 'User updated'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

   