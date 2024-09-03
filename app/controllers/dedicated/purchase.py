import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import *
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
                    result = self.purchase_item(self.entry, result)
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
    def purchase_item(self, entry=None, result=None):
        """This function is a special case. The coding structure might be different from the standard."""
        try:
            currentDate = datetime.now()
            member = entry['member']
            orderItem = entry['order']['item']
            
            organizationId = entry['organization']['id']
            userId = entry['user']['id']
            memberId = member['id'] if member is not None else None
            dateId = Date.get_or_none(Date.DateValue == currentDate).Id
            orderTypeId = OrderType.get_or_none(OrderType.OrderTypeName == entry['order']['type']).Id
            referenceId = entry['order']['referenceId']
            orderName = entry['order']['name']
            orderSummary = entry['summary']
            orderPayment = entry['payment']
            
            receipt = Receipt.create(
                OrganizationId=organizationId,
                UserId=userId,
                MemberId=memberId,
                DateId=dateId,
                OrderTypeId=orderTypeId,
                ReferenceId=referenceId,
                OrderName=orderName,
                OrderSummary=orderSummary,
                OrderPayment=orderPayment,
            )
            
            for item in orderItem:
                itemSold = ItemSold.create(
                    ReceiptId=receipt.Id,
                    ItemId=item['itemId'],
                    Quantity=item['quantity'],
                    Total=item['total'],
                    StockBypass=item['stockBypass'],
                )

            result['success'] = True
            result['dictData'] = entry
            result['message'] = 'Purchase added'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result

    