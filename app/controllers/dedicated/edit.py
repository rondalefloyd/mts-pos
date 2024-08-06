import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import (
    User,
    Member,
    Reward,
    Promo,
    ItemType,
    Brand,
    Supplier,
    SalesGroup,
    Item,
    ItemPrice,
    Stock,
)
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
                if self.function_route == 'edit_item_price_related_data_by_id':
                    result = edit_item_price_related_data_by_id(self.entry, result)
                elif self.function_route == 'edit_member_data_by_id':
                    result = edit_member_data_by_id(self.entry, result)
                elif self.function_route == 'edit_promo_data_by_id':
                    result = edit_promo_data_by_id(self.entry, result)
                elif self.function_route == 'edit_reward_data_by_id':
                    result = edit_reward_data_by_id(self.entry, result)
                elif self.function_route == 'edit_stock_data_by_id':
                    result = edit_stock_data_by_id(self.entry, result)
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
def edit_item_price_related_data_by_id(entry=None, result=None):
    # TODO: finish this
    try:
        print('this is the entry:', entry)
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

        # applying promo
        itemPrice = ItemPrice.get_or_none(ItemPrice.Id == entry['itemPriceId'])
        
        if entry['applyPromo'] == 'True' and entry['promoId'] != 'None':
            result['message'] = 'Item already has promo'
            return result

        elif entry['applyPromo'] == 'True' and entry['promoId'] == 'None':
            itemPrice.ItemId = item.Id
            itemPrice.Capital = entry['capital']
            itemPrice.Price = entry['price']
            itemPrice.EffectiveDate = datetime.strptime(entry['endDate'], '%Y-%m-%d') + timedelta(days=1)
            itemPrice.UpdateTs = datetime.now()
            itemPrice.save()
            
            itemPrice = ItemPrice.create(
                ItemId=item.Id,
                Capital=entry['capital'],
                Price=entry['newPrice'],
                PromoId=Promo.get_or_none(Promo.PromoName == entry['promoName']).Id,
                Discount=entry['discount'],
                EffectiveDate=entry['startDate'],
            )
            
        else:
            itemPrice.ItemId = item.Id
            itemPrice.Capital = entry['capital']
            itemPrice.Price = entry['price']
            itemPrice.EffectiveDate = entry['effectiveDate']
            itemPrice.save()
            
        # applying stock
        if entry['trackInventory'] == 'True' and entry['stockId'] != 'None':
            result['message'] = 'Item already has stock'
            return result
        
        elif entry['trackInventory'] == 'True' and entry['stockId'] == 'None':
            stock = Stock.create(ItemId=item.Id)
            
        else:
            stock = Stock.get_or_none(Stock.ItemId == item.Id).delete_instance()
        
        result['success'] = True
        result['message'] = 'ItemPrice updated'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def edit_member_data_by_id(entry=None, result=None):
    try:
        member = Member.select().where(Member.MemberName == entry['memberName'])
        
        if member.exists():
            result['message'] = 'Member already exists'
            return result
            
        member = Member.get_or_none(Member.Id == entry['id'])
        member.MemberName = entry['memberName']
        member.BirthDate = entry['birthDate']
        member.Address = entry['address']
        member.MobileNumber = entry['mobileNumber']
        member.Points = entry['points']
        member.save()
        
        result['success'] = True
        result['message'] = 'Member updated'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def edit_promo_data_by_id(entry=None, result=None):
    try:
        promo = Promo.select().where(Promo.PromoName == entry['promoName'])
        
        if promo.exists():
            result['message'] = 'Promo already exists'
            return result
            
        promo = Promo.get_or_none(Promo.Id == entry['id'])
        promo.PromoName = entry['promoName']
        promo.DiscountRate = entry['discountRate']
        promo.Description = entry['description']
        promo.save()
        
        result['success'] = True
        result['message'] = 'Promo updated'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result
    
def edit_reward_data_by_id(entry=None, result=None):
    try:
        reward = Reward.select().where(Reward.RewardName == entry['rewardName'])
        
        if reward.exists():
            result['message'] = 'Reward already exists'
            return result
            
        reward = Reward.get_or_none(Reward.Id == entry['id'])
        reward.RewardName = entry['rewardName']
        reward.Points = entry['points']
        reward.Target = entry['target']
        reward.Description = entry['description']
        reward.save()
        
        result['success'] = True
        result['message'] = 'Reward updated'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result

def edit_stock_data_by_id(entry=None, result=None):
    try:
        stock = Stock.get_or_none(Stock.Id == entry['id'])
        stock.OnHand = entry['onHand']
        stock.Available = entry['available']
        stock.save()
        
        result['success'] = True
        result['message'] = 'Stock updated'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result