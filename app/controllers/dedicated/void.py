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
    ItemSold,
    Reason
)
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
                if self.function_route == 'void_item_sold_data_by_id':
                    result = void_item_sold_data_by_id(self.entry, result)
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
        # print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))
        
def void_item_sold_data_by_id(entry=None, result=None):
    try:
        itemSold = ItemSold.select().where(
            (ItemSold.Id == entry['id']) &
            (ItemSold.Status == 1)
        )
        
        if itemSold.exists():
            result['message'] = 'ItemSold already voided'
            return result
        
        itemSold = ItemSold.get_or_none(ItemSold.Id == entry['id'])
        itemSold.ReasonId = Reason.get_or_none(Reason.ReasonName == entry['reasonName']).Id
        itemSold.Status = 1
        itemSold.save()
        
        # TODO: add stock by taking it from qty (depending on the condition if it got bypassed or not)
        # TODO: change the computation of the summary (deduct the ones that are voided)
        
        result['success'] = True
        result['message'] = 'ItemSold voided'
        return result
        
    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result

    