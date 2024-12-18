import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import *
from app.utils.databases import postgres_db


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
            'dictData': {},
            'listData': [],
        }
         
        try:
            with postgres_db:
                if self.function_route == 'registerProduct':
                    result = self.registerProduct(self.entry, result)
                elif self.function_route == 'registerItem':
                    result = self.registerItem(self.entry, result)
                elif self.function_route == 'registerBrand':
                    result = self.registerBrand(self.entry, result)
                elif self.function_route == 'registerItemType':
                    result = self.registerItemType(self.entry, result)
                elif self.function_route == 'registerSupplier':
                    result = self.registerSupplier(self.entry, result)
                elif self.function_route == 'registerMember':
                    result = self.registerMember(self.entry, result)
                elif self.function_route == 'registerPromo':
                    result = self.registerPromo(self.entry, result)
                elif self.function_route == 'registerReward':
                    result = self.registerReward(self.entry, result)
                elif self.function_route == 'registerUser':
                    result = self.registerUser(self.entry, result)
                elif self.function_route == 'registerOrganization':
                    result = self.registerOrganization(self.entry, result)
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
        print(f"{self.function_route} -> result_message: {result['message']}")

    # add function here
    def registerProduct(self, entry=None, result=None):
        print('this is the register item')
        """This function is a special case. The coding structure might be different from the standard."""
        try:
            entry['itemName'] = entry['itemName'] if entry['itemName'] != '' else '-'
            entry['barcode'] = entry['barcode'] if entry['barcode'] != '' else '-'
            entry['itemTypeName'] = entry['itemTypeName'] if entry['itemTypeName'] != '' else '-'
            entry['brandName'] = entry['brandName'] if entry['brandName'] != '' else '-'
            entry['supplierName'] = entry['supplierName'] if entry['supplierName'] != '' else '-'
            entry['cost'] = entry['cost'] if entry['cost'] != '' else '0'
            entry['retailPrice'] = entry['retailPrice'] if entry['retailPrice'] != '' else '0'
            entry['wholesalePrice'] = entry['wholesalePrice'] if entry['wholesalePrice'] != '' else '0'
            
            itemType = ItemType.select().where(ItemType.ItemTypeName == entry['itemTypeName'])
            brand = Brand.select().where(Brand.BrandName == entry['brandName'])
            supplier = Supplier.select().where(Supplier.SupplierName == entry['supplierName'])
            
            itemType = ItemType.create(ItemTypeName=entry['itemTypeName']) if not itemType.exists() else itemType.first()
            brand = Brand.create(BrandName=entry['brandName']) if not brand.exists() else brand.first()
            supplier = Supplier.create(SupplierName=entry['supplierName']) if not supplier.exists() else supplier.first()
            
            salesGroupEntries = [
                {'salesGroupName': 'retail'.upper(), 'salesGroupPrice': entry['retailPrice']},
                {'salesGroupName': 'wholesale'.upper(), 'salesGroupPrice': entry['wholesalePrice']},
            ]
            
            for salesGroupEntry in salesGroupEntries:
                item = Item.select().where(
                    (Item.ItemName == entry['itemName']) &
                    (Item.Barcode == entry['barcode']) &
                    (Item.ExpireDate == entry['expireDate']) &
                    (Item.ItemTypeId == itemType.Id) &
                    (Item.BrandId == brand.Id) &
                    (Item.SupplierId == supplier.Id) &
                    (Item.SalesGroupId == SalesGroup.get_or_none(SalesGroup.SalesGroupName == salesGroupEntry['salesGroupName']).Id)
                )
                
                # if item.exists():
                #     result['message'] = 'Item already exists'
                #     return result
                
                item = Item.create(
                    ItemName=entry['itemName'],
                    Barcode=entry['barcode'],
                    ExpireDate=entry['expireDate'],
                    ItemTypeId=itemType.Id,
                    BrandId=brand.Id,
                    SupplierId=supplier.Id,
                    SalesGroupId=SalesGroup.get_or_none(SalesGroup.SalesGroupName == salesGroupEntry['salesGroupName']).Id,
                ) if not item.exists() else item.first()
                
                itemPrice = ItemPrice.select().where(
                    (ItemPrice.ItemId == item.Id) &
                    (ItemPrice.Price == salesGroupEntry['salesGroupPrice']) & 
                    (ItemPrice.EffectiveDate == entry['effectiveDate']) 
                )
            
                if itemPrice.exists():
                    result['message'] = 'ItemPrice already exists'
                    return result
                
                itemPrice = ItemPrice.create(
                    ItemId=item.Id,
                    Cost=entry['cost'],
                    Price=salesGroupEntry['salesGroupPrice'], 
                    EffectiveDate=entry['effectiveDate'],
                )
            
                if entry['trackInventory'] is True:
                    stock = Stock.create(ItemId=item.Id)
            
            result['success'] = True
            result['message'] = 'Item added'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

    def registerMember(self, entry=None, result=None):
        try:
            entry['organizationName'] = entry['organizationName'] if entry['organizationName'] != '' else '-'
            entry['memberName'] = entry['memberName'] if entry['memberName'] != '' else '-'
            entry['address'] = entry['address'] if entry['address'] != '' else '-'
            entry['mobileNumber'] = entry['mobileNumber'] if entry['mobileNumber'] != '' else '-'
            entry['points'] = entry['points'] if entry['points'] != '' else '0'
            
            member = Member.select().where(
                (Member.OrganizationId == Organization.get_or_none(Organization.OrganizationName == entry['organizationName']).Id) &
                (Member.MemberName == entry['memberName']) &
                (Member.BirthDate == entry['birthDate']) &
                (Member.Address == entry['address']) &
                (Member.MobileNumber == entry['mobileNumber']) &
                (Member.Points == entry['points'])
            )
            
            if member.exists():
                result['message'] = 'Member already exists'
                return result
            
            member = Member.create(
                OrganizationId=Organization.get_or_none(Organization.OrganizationName == entry['organizationName']).Id,
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
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def registerPromo(self, entry=None, result=None):
        try:
            entry['promoName'] = entry['promoName'] if entry['promoName'] != '' else '-'
            entry['discountRate'] = entry['discountRate'] if entry['discountRate'] != '' else '0'
            entry['description'] = entry['description'] if entry['description'] != '' else '-'
            
            promo = Promo.select().where(
                (Promo.PromoName == entry['promoName']) &
                (Promo.DiscountRate == entry['discountRate']) &
                (Promo.Description == entry['description'])
            )
            
            if promo.exists():
                result['message'] = 'Promo already exists'
            
            promo = Promo.create(
                PromoName=entry['promoName'],
                DiscountRate=entry['discountRate'],
                Description=entry['description'],
            )
            
            result['success'] = True
            result['message'] = 'Promo added'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
                       
    def registerItem(self, entry=None, result=None):
        try:
            entry['itemName'] = entry['itemName'] if entry['itemName'] != '' else '-'
            entry['barcode'] = entry['barcode'] if entry['barcode'] != '' else '-'
            entry['itemTypeName'] = entry['itemTypeName'] if entry['itemTypeName'] != '' else '-'
            entry['brandName'] = entry['brandName'] if entry['brandName'] != '' else '-'
            entry['supplierName'] = entry['supplierName'] if entry['supplierName'] != '' else '-'
            entry['salesGroupName'] = entry['salesGroupName'] if entry['salesGroupName'] != '' else '-'
            
            item = Item.select().where(
                (Item.Barcode == entry['barcode']) &
                (Item.ItemTypeId == ItemType.get_or_none(ItemType.ItemTypeName == entry['itemTypeName']).Id) &
                (Item.BrandId == Brand.get_or_none(Brand.BrandName == entry['brandName']).Id) &
                (Item.SupplierId == Supplier.get_or_none(Supplier.SupplierName == entry['supplierName']).Id) &
                (Item.SalesGroupId == SalesGroup.get_or_none(SalesGroup.SalesGroupName == entry['salesGroupName']).Id)
            )
            
            if item.exists():
                result['message'] = 'Item already exists'
            
            item = Item.create(
                ItemName=entry['itemName'],
                Barcode=entry['barcode'],
                ExpireDate=entry['expireDate'],
                ItemTypeId=ItemType.get_or_none(ItemType.ItemTypeName == entry['itemTypeName']).Id,
                BrandId=Brand.get_or_none(Brand.BrandName == entry['brandName']).Id,
                SupplierId=Supplier.get_or_none(Supplier.SupplierName == entry['supplierName']).Id,
                SalesGroupId=SalesGroup.get_or_none(SalesGroup.SalesGroupName == entry['salesGroupName']).Id,
            )
            
            result['success'] = True
            result['message'] = 'Item added'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
               
    def registerBrand(self, entry=None, result=None):
        try:
            entry['brandName'] = entry['brandName'] if entry['brandName'] != '' else '-'
            
            brand = Brand.select().where((Brand.BrandName == entry['brandName']))
            
            if brand.exists():
                result['message'] = 'Brand already exists'
            
            brand = Brand.create(BrandName=entry['brandName'])
            
            result['success'] = True
            result['message'] = 'Brand added'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
                       
    def registerItemType(self, entry=None, result=None):
        try:
            entry['itemTypeName'] = entry['itemTypeName'] if entry['itemTypeName'] != '' else '-'
            
            itemType = ItemType.select().where((ItemType.ItemTypeName == entry['itemTypeName']))
            
            if itemType.exists():
                result['message'] = 'ItemType already exists'
            
            itemType = ItemType.create(ItemTypeName=entry['itemTypeName'])
            
            result['success'] = True
            result['message'] = 'ItemType added'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
                       
    def registerSupplier(self, entry=None, result=None):
        try:
            entry['supplierName'] = entry['supplierName'] if entry['supplierName'] != '' else '-'
            
            supplier = Supplier.select().where((Supplier.SupplierName == entry['supplierName']))
            
            if supplier.exists():
                result['message'] = 'Supplier already exists'
            
            supplier = Supplier.create(SupplierName=entry['supplierName'])
            
            result['success'] = True
            result['message'] = 'Supplier added'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def registerReward(self, entry=None, result=None):
        try:
            entry['rewardName'] = entry['rewardName'] if entry['rewardName'] != '' else '-'
            entry['points'] = entry['points'] if entry['points'] != '' else '0'
            entry['target'] = entry['target'] if entry['target'] != '' else '0'
            entry['description'] = entry['description'] if entry['description'] != '' else '-'
            
            reward = Reward.select().where(
                (Reward.RewardName == entry['rewardName']) &
                (Reward.Points == entry['points']) &
                (Reward.Target == entry['target']) &
                (Reward.Description == entry['description'])
            )
            
            if reward.exists():
                result['message'] = 'Reward already exists'
            
            reward = Reward.create(
                RewardName=entry['rewardName'],
                Points=entry['points'] if entry['points'] != '' else 0,
                Target=entry['target'] if entry['target'] != '' else 0,
                Description=entry['description'],
            )
            
            result['success'] = True
            result['message'] = 'Reward added'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def registerUser(self, entry=None, result=None):
        try:
            entry['userName'] = entry['userName'] if entry['userName'] != '' else '-'
            entry['password'] = entry['password'] if entry['password'] != '' else '-'
            entry['fullName'] = entry['fullName'] if entry['fullName'] != '' else '-'
            entry['mobileNumber'] = entry['mobileNumber'] if entry['mobileNumber'] != '' else '-'
            
            user = User.select().where(
                (User.OrganizationId == Organization.get_or_none(Organization.OrganizationName == entry['organizationName']).Id) &
                (User.UserName == entry['userName']) &
                (User.Password == entry['password']) &
                (User.FullName == entry['fullName']) &
                (User.BirthDate == entry['birthDate']) &
                (User.MobileNumber == entry['mobileNumber']) &
                (User.AccessLevel == entry['accessLevel'])
            )
            
            if user.exists():
                result['message'] = 'User already exists'
                return result
            
            user = User.create(
                OrganizationId=Organization.get_or_none(Organization.OrganizationName == entry['organizationName']).Id,
                UserName=entry['userName'],
                Password=entry['password'],
                FullName=entry['fullName'],
                BirthDate=entry['birthDate'],
                MobileNumber=entry['mobileNumber'],
                AccessLevel=entry['accessLevel'],
            )
            
            userSessionInfo = UserSession.create(
                UserId=user.Id,
                ActiveStatus=0,
                LastLoginTs=datetime.now(),
            )
            
            result['success'] = True
            result['message'] = 'User added'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def registerOrganization(self, entry=None, result=None):
        try:
            entry['taxId'] = entry['taxId'] if entry['taxId'] != '' else '-'
            entry['organizationName'] = entry['organizationName'] if entry['organizationName'] != '' else '-'
            entry['address'] = entry['address'] if entry['address'] != '' else '-'
            entry['mobileNumber'] = entry['mobileNumber'] if entry['mobileNumber'] != '' else '-'

            organization = Organization.select().where(
                (Organization.TaxId == entry['taxId']) &
                (Organization.OrganizationName == entry['organizationName']) &
                (Organization.Address == entry['address']) &
                (Organization.MobileNumber == entry['mobileNumber']) &
                (Organization.Password == entry['password'])
            )
            
            if organization.exists():
                result['message'] = 'Organization already exists'
            
            organization = Organization.create(
                TaxId=entry['taxId'],
                OrganizationName=entry['organizationName'],
                Address=entry['address'],
                MobileNumber=entry['mobileNumber'],
                Password=entry['password'],
            )
            
            result['success'] = True
            result['message'] = 'Organization added'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    
