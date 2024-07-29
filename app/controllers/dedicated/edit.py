import os, sys, logging
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import (
    Users,
    Members,
    Rewards,
    Promos,
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
        }
        try:
            with postgres_db:
                match self.function_route:
                    case 'pos/edit/user/id':
                        result = edit_user_by_id(self.entry)
                    case 'pos/edit/member/id':
                        result = edit_member_by_id(self.entry)
                    case 'pos/edit/promo/id':
                        result = edit_promo_by_id(self.entry)
                    case 'pos/edit/reward/id':
                        result = edit_reward_by_id(self.entry)
                    case 'pos/edit/item/id':
                        result = edit_item_by_id(self.entry)
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

def edit_user_by_id(entry):
    result = {
        'success': False,
        'message': 'Update failed.',
    }
    
    if entry_has_value(alpha_entry=['organizationId', 'userName', 'accessCode', 'fullName', 'birthDate', 'mobileNumber', 'accessLevel'], entry=entry) is False:
        result['message'] = 'Invalid entry.'
        return result
    
    try:
        # Check if the user to update exists by ID
        users = Users.select().where(Users.Id == entry['id'])
        
        if not users.exists():
            result['message'] = 'User does not exist.'
            return result
        
        user = users.first()
        
        # Update user details
        user.OrganizationId = entry['organizationId']
        user.UserName = entry['userName']
        user.AccessCode = entry['accessCode']
        user.FullName = entry['fullName']
        user.BirthDate = entry['birthDate']
        user.MobileNumber = entry['mobileNumber']
        user.AccessLevel = entry['accessLevel']
        user.save()  # Save the changes to the database
        
        result['success'] = True
        result['message'] = 'User updated successfully.'
        
    except IntegrityError as error:
        result['message'] = integrity_error_message(error)
        logging.error(error)
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        logging.error(error)
         
    return result

def edit_member_by_id(entry):
    result = {
        'success': False,
        'message': 'Update failed.',
    }
    
    if entry_has_value(alpha_entry=['memberName', 'birthDate', 'address', 'mobileNumber', 'points'], entry=entry) is False:
        result['message'] = 'Invalid entry.'
        return result
    
    try:
        # Check if the member to update exists by ID
        members = Members.select().where(Members.Id == entry['id'])
        
        if not members.exists():
            result['message'] = 'Member does not exist.'
            return result
        
        members = members.first()
        
        # Update member details
        members.MemberName = entry['memberName']
        members.BirthDate = entry['birthDate']
        members.Address = entry['address']
        members.MobileNumber = entry['mobileNumber']
        members.Points = entry['points']
        members.save()  # Save the changes to the database
        
        result['success'] = True
        result['message'] = 'Member updated successfully.'
        
    except IntegrityError as error:
        result['message'] = integrity_error_message(error)
        logging.error(error)
        
    except Exception as error:
        result['message'] = exception_error_message(error)
         
    return result

def edit_promo_by_id(entry):
    result = {
        'success': False,
        'message': 'Update failed.',
    }
    
    if entry_has_value(alpha_entry=['promoName', 'discountRate', 'description'], entry=entry) is False:
        result['message'] = 'Invalid entry.'
        return result
    
    try:
        # Check if the promo to update exists by ID
        promos = Promos.select().where(Promos.Id == entry['id'])
        
        if not promos.exists():
            result['message'] = 'Promo does not exist.'
            return result
        
        promo = promos.first()
        
        # Update promo details
        promo.PromoName = entry['promoName']
        promo.DiscountRate = entry['discountRate']
        promo.Description = entry['description']
        promo.save()  # Save the changes to the database
        
        result['success'] = True
        result['message'] = 'Promo updated successfully.'
        
    except IntegrityError as error:
        result['message'] = integrity_error_message(error)
        logging.error(error)
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        logging.error(error)
         
    return result

def edit_reward_by_id(entry):
    result = {
        'success': False,
        'message': 'Update failed.',
    }
    
    if entry_has_value(alpha_entry=['rewardName', 'points', 'target', 'description'], entry=entry) is False:
        result['message'] = 'Invalid entry.'
        return result
    
    try:
        # Check if the reward to update exists by ID
        rewards = Rewards.select().where(Rewards.Id == entry['id'])
        
        if not rewards.exists():
            result['message'] = 'Reward does not exist.'
            return result
        
        reward = rewards.first()
        
        # Update reward details
        reward.RewardName = entry['rewardName']
        reward.Points = entry['points']
        reward.Target = entry['target']
        reward.Description = entry['description']
        reward.save()  # Save the changes to the database
        
        result['success'] = True
        result['message'] = 'Reward updated successfully.'
        
    except IntegrityError as error:
        result['message'] = integrity_error_message(error)
        logging.error(error)
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        logging.error(error)
         
    return result

def edit_item_by_id(entry):
    result = {
        'success': False,
        'message': 'Update failed.',
    }
    
    if entry_has_value(
        alpha_entry=['itemName', 'barcode', 'itemTypeName', 'brandName', 'supplierName', 'salesGroupName', 'promoName'], 
        numeric_entry=['capital', 'price', 'discountRate', 'discount', 'price', 'newPrice'],
        entry=entry,
    ) is False:
        result['message'] = 'Invalid entry.'
        return result
    
    try:
        # Check if the reward to update exists by ID
        itemTypes = ItemTypes.select().where(ItemTypes.ItemTypeName == entry['itemTypeName'])
        brands = Brands.select().where(Brands.BrandName == entry['brandName'])
        suppliers = Suppliers.select().where(Suppliers.SupplierName == entry['supplierName'])
        salesGroups = SalesGroups.select().where(SalesGroups.SalesGroupName == entry['salesGroupName'])
        items = Items.select().where(Items.ItemName == entry['itemId'])
        itemPrices = ItemPrices.select().where(ItemPrices.ItemPriceId == entry['id'])

        if not itemTypes.exists():
            result['message'] = 'ItemType does not exist.'
            return result
        if not brands.exists():
            result['message'] = 'Brand does not exist.'
            return result
        if not suppliers.exists():
            result['message'] = 'Supplier does not exist.'
            return result
        if not salesGroups.exists():
            result['message'] = 'SalesGroup does not exist.'
            return result
        if not items.exists():
            result['message'] = 'Item does not exist.'
            return result
        if not itemPrices.exists():
            result['message'] = 'ItemPrice does not exist.'
            return result
        
        itemTypes = itemTypes.first()
        itemTypes.ItemTypeName = entry['itemTypeName']
        itemTypes.save()
        
        brands = brands.first()
        brands.BrandName = entry['brandName']
        brands.save()
        
        suppliers = suppliers.first()
        suppliers.SupplierName = entry['supplierName']
        suppliers.save()
        
        salesGroups = salesGroups.first()
        salesGroups.SalesGroupName = entry['salesGroupName']
        salesGroups.save()
        
        items = items.first()
        items.ItemName = entry['itemName']
        items.Barcode = entry['barcode']
        items.ExpireDate = entry['expireDate']
        items.ItemTypeId = ItemTypes.select(ItemTypes.Id).where(ItemTypes.ItemTypeName == entry['itemTypeName']).first()
        items.BrandId = Brands.select(Brands.Id).where(Brands.BrandName == entry['brandName']).first()
        items.SupplierId = Suppliers.select(Suppliers.Id).where(Suppliers.SupplierName == entry['supplierName']).first()
        items.SalesGroupId = SalesGroups.select(SalesGroups.Id).where(SalesGroups.SalesGroupName == entry['salesGroupName']).first()
        items.save()
        
        if entry['promoName'] != 'N/A':
            itemPrices = ItemPrices.create(
                ItemId=items.Id,
                Capital=entry['capital'],
                Price=entry['newPrice'],
                PromoId=Promos.select(Promos.Id).where(Promos.PromoName == entry['promoName']).first(),
                Discount=entry['discount'],
                EffectiveDate=entry['startDate'],
            )
            
            itemPrices = ItemPrices.create(
                ItemId=items.Id,
                Capital=entry['capital'],
                Price=entry['price'],
                EffectiveDate=datetime.strptime(entry['endDate'], '%Y-%m-%d').date() + timedelta(days=1),
            )
        
        else:
            itemPrices = itemPrices.first()
            itemPrices.ItemId = entry['itemId']
            itemPrices.Capital = entry['capital']
            itemPrices.Price = entry['price']
            itemPrices.PromoId = Promos.select(Promos.Id).where(Promos.PromoName == entry['promoName']).first()
            itemPrices.Discount = entry['discount']
            itemPrices.EffectiveDate = entry['effectiveDate']
            items.save()
        
        result['success'] = True
        result['message'] = 'Reward updated successfully.'
        
    except IntegrityError as error:
        result['message'] = integrity_error_message(error)
        logging.error(error)
        
    except Exception as error:
        result['message'] = exception_error_message(error)
        logging.error(error)
         
    return result

