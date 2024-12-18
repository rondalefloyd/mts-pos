import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import *
from app.utils.databases import postgres_db


class VoidThread(QThread):
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
                if self.function_route == 'voidItemSoldDataById':
                    result = self.voidItemSoldDataById(self.entry, result)
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
        
    def voidItemSoldDataById(self, entry=None, result=None):
        try:
            itemSold = ItemSold.select().where(
                (ItemSold.Id == entry['id']) &
                (ItemSold.VoidStatus == 1)
            )
            
            if itemSold.exists():
                result['message'] = 'ItemSold already voided'
                return result
            
            itemSold = ItemSold.get_or_none(ItemSold.Id == entry['id'])
            itemSold.VoidReason = entry['reasonName']
            itemSold.VoidStatus = 1
            itemSold.save()
            
            receipt = Receipt.get_or_none(Receipt.Id == itemSold.ReceiptId)
            receipt.Billing['subtotal'] -= itemSold.Total
            receipt.Billing['grandtotal'] = (receipt.Billing['subtotal'] + receipt.Billing['discount']) + receipt.Billing['tax']
            receipt.Billing['change'] -= itemSold.Total
            receipt.save()
            
            stock = Stock.select().where(Stock.ItemId == entry['itemId'])
            
            if stock.exists() and entry['stockBypass'] == 0:
                stock = stock.first()
                stock.Available += entry['quantity']
                stock.save()

            
            result['success'] = True
            result['message'] = f"ItemSold voided. Amount to return: {itemSold.Total}"
            return result
            
        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

    