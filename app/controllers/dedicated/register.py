import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import (
    User, 
    UserSession, 
    Organization,
    Member,
    Promo,
    Reward,
    ItemType,
    Brand,
    Supplier,
    SalesGroup,
    Item,
    ItemPrice,
    Stock,
)
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
                if self.function_route == 'register_item':
                    result = register_item(self.entry, result)
                elif self.function_route == 'register_member':
                    result = register_member(self.entry, result)
                elif self.function_route == 'register_promo':
                    result = register_promo(self.entry, result)
                elif self.function_route == 'register_reward':
                    result = register_reward(self.entry, result)
                elif self.function_route == 'register_user':
                    result = register_user(self.entry, result)
                elif self.function_route == 'register_organization':
                    result = register_organization(self.entry, result)
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
        # print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))

# add function here
def register_item(entry=None, result=None):
    """This function is a special case. The coding structure might be different from the standard."""
    try:
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
                Capital=entry['capital'],
                Price=salesGroupEntry['salesGroupPrice'], 
                EffectiveDate=entry['effectiveDate'],
            )
        
            if entry['trackInventory'] is 'True':
                stock = Stock.create(ItemId=item.Id)
        
        result['success'] = True
        result['message'] = 'Item added'
        return result

    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result

def register_member(entry=None, result=None):
    try:
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
    
def register_promo(entry=None, result=None):
    try:
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
    
def register_reward(entry=None, result=None):
    try:
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
            Points=entry['points'],
            Target=entry['target'],
            Description=entry['description'],
        )
        
        result['success'] = True
        result['message'] = 'Reward added'
        return result

    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def register_user(entry=None, result=None):
    try:
        user = User.select().where(
            (User.OrganizationId == Organization.get_or_none(Organization.OrganizationName == entry['organizationName']).Id) &
            (User.UserName == entry['userName']) &
            (User.AccessCode == entry['accessCode']) &
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
            AccessCode=entry['accessCode'],
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
    
def register_organization(entry=None, result=None):
    try:
        organization = Organization.select().where(
            (Organization.TaxId == entry['taxId']) &
            (Organization.OrganizationName == entry['organizationName']) &
            (Organization.Address == entry['address']) &
            (Organization.MobileNumber == entry['mobileNumber']) &
            (Organization.AccessCode == entry['accessCode'])
        )
        
        if organization.exists():
            result['message'] = 'Organization already exists'
        
        organization = Organization.create(
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
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result