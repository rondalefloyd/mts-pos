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
    ItemSold
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

    