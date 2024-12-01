import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import *
from app.utils.databases import postgres_db

class RemoveThread(QThread):
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
                if self.function_route == 'removeItemPriceById':
                    result = self.removeItemPriceById(self.entry, result)
                elif self.function_route == 'removeItemById':
                    result = self.removeItemById(self.entry, result)
                elif self.function_route == 'removeBrandById':
                    result = self.removeBrandById(self.entry, result)
                elif self.function_route == 'removeItemTypeById':
                    result = self.removeItemTypeById(self.entry, result)
                elif self.function_route == 'removeSupplierById':
                    result = self.removeSupplierById(self.entry, result)
                elif self.function_route == 'removeStockById':
                    result = self.removeStockById(self.entry, result)
                elif self.function_route == 'removeMemberById':
                    result = self.removeMemberById(self.entry, result)
                elif self.function_route == 'removePromoById':
                    result = self.removePromoById(self.entry, result)
                elif self.function_route == 'removeRewardById':
                    result = self.removeRewardById(self.entry, result)
                elif self.function_route == 'removeUserById':
                    result = self.removeUserById(self.entry, result)
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
    def removeItemPriceById(self, entry=None, result=None):
        try:
            itemPrice = ItemPrice.select().where(ItemPrice.Id == entry['itemPriceId'])
            
            if not itemPrice.exists():
                result['message'] = 'ItemPrice does not exists'
                return
            
            itemPrice = itemPrice.get_or_none().delete_instance()
            
            result['success'] = True
            result['message'] = 'ItemPrice deleted'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def removeItemById(self, entry=None, result=None):
        try:
            item = Item.select().where(Item.Id == entry['id'])
            
            if not item.exists():
                result['success'] = False
                result['message'] = 'Item does not exists'
                return result
            
            itemPrice = ItemPrice.get_or_none(ItemPrice.ItemId == entry['id'])
            
            if itemPrice is not None:
                result['message'] = 'Item is being used. Remove the prices that uses this first.'
                return result
            
            itemSold = ItemSold.get_or_none(ItemSold.ItemId == entry['id'])
                
            if itemSold is not None:
                result['message'] = 'Item is being used. Remove the transactions that uses this first.'
                return result
                
            item = item.get_or_none().delete_instance()
            
            result['success'] = True
            result['message'] = 'Item deleted'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def removeBrandById(self, entry=None, result=None):
        try:
            brand = Brand.select().where(Brand.Id == entry['id'])
            
            if not brand.exists():
                result['success'] = False
                result['message'] = 'Brand does not exists'
                return result
            
            item = Item.get_or_none(Item.BrandId == entry['id'])
            
            if item is not None:
                result['message'] = 'Brand is being used. Remove the items that uses this first.'
                return result
                
            brand = brand.get_or_none().delete_instance()
            
            result['success'] = True
            result['message'] = 'Brand deleted'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

    def removeItemTypeById(self, entry=None, result=None):
        try:
            itemType = ItemType.select().where(ItemType.Id == entry['id'])
            
            if not itemType.exists():
                result['success'] = False
                result['message'] = 'ItemType does not exists'
                return
            
            item = Item.get_or_none(Item.ItemTypeId == entry['id'])
            
            if item is not None:
                result['message'] = 'ItemType is being used. Remove the items that uses this first.'
                return result
                
            itemType = itemType.get_or_none().delete_instance()
            
            result['success'] = True
            result['message'] = 'ItemType deleted'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def removeSupplierById(self, entry=None, result=None):
        try:
            supplier = Supplier.select().where(Supplier.Id == entry['id'])
            
            if not supplier.exists():
                result['success'] = False
                result['message'] = 'Supplier does not exists'
                return
            
            item = Item.get_or_none(Item.SupplierId == entry['id'])
            
            if item is not None:
                result['message'] = 'Supplier is being used. Remove the items that uses this first.'
                return result
            
            supplier = supplier.get_or_none().delete_instance()
            
            result['success'] = True
            result['message'] = 'Supplier deleted'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
        
    def removeStockById(self, entry=None, result=None):
        try:
            stock = Stock.select().where(Stock.Id == entry['id'])
            
            if not stock.exists():
                result['message'] = 'Stock does not exists'
                return
            
            stock = stock.get_or_none().delete_instance()
            
            result['success'] = True
            result['message'] = 'Stock deleted'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

    def removeMemberById(self, entry=None, result=None):
        try:
            member = Member.select().where(Member.Id == entry['id'])
            
            if not member.exists():
                result['message'] = 'Member does not exists'
                return
            
            member = member.get_or_none().delete_instance()
            
            result['success'] = True
            result['message'] = 'Member deleted'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def removePromoById(self, entry=None, result=None):
        try:
            promo = Promo.select().where(Promo.Id == entry['id'])
            
            if not promo.exists():
                result['message'] = 'Promo does not exists'
                return
            
            itemPrice = ItemPrice.get_or_none(ItemPrice.PromoId == entry['id'])
            
            if itemPrice is not None:
                result['message'] = 'Promo is being used. Remove the prices that uses this first.'
                return result
            
            promo = promo.get_or_none().delete_instance()
            
            result['success'] = True
            result['message'] = 'Promo deleted'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def removeRewardById(self, entry=None, result=None):
        try:
            reward = Reward.select().where(Reward.Id == entry['id'])
            
            if not reward.exists():
                result['message'] = 'Reward does not exists'
                return
            
            reward = reward.get_or_none().delete_instance()
            
            result['success'] = True
            result['message'] = 'Reward deleted'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
    def removeUserById(self, entry=None, result=None):
        try:
            user = User.select().where(User.Id == entry['id'])
            
            if not user.exists():
                result['message'] = 'User does not exists'
                return
            
            user = user.get_or_none().delete_instance()
            
            result['success'] = True
            result['message'] = 'User deleted'
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
    
    
    
    