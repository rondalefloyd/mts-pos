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
    ItemSold,
    Receipt
)
from app.utils.databases import postgres_db


class PurchaseThread(QThread):
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
                if self.function_route == 'purchase_item':
                    result = purchase_item(self.entry, result)
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
        print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))

# add function here
def purchase_item(entry=None, result=None):
    """This function is a special case. The coding structure might be different from the standard."""
    try:
        print('---check this entry:', json.dumps(entry, indent=4, default=str))
        orderName = entry['orderName']
        orderType = entry['orderType']
        orderItem = entry['orderItem']
        orderWidget = entry['orderWidget']
        orderStatus = entry['orderStatus']
        orderMember = entry['orderMember']
        
        # TODO: finish this
        # receipt = Receipt.create(
        #     OrganizationId=1123,
        #     UserId=1123,
        #     MemberId=1123,
        #     DateId=1123,
        #     OrderTypeId=1123,
        #     ReferenceId=1123,
        #     OrderName=1123,
        #     OrderSummary=1123,
        #     OrderPayment=1123,
        # )
        # itemSold = ItemSold

        result['success'] = True
        result['message'] = 'Purchase added'
        return result

    except Exception as exception:
        result['success'] = False
        result['message'] = f"An error occured: {exception}"
        return result

    