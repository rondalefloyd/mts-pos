import os, sys, logging, math, json, pandas as pd
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import *
from app.utils.databases import postgres_db


class LoadThread(QThread):
    running = pyqtSignal(object)
    finished = pyqtSignal(object)
    
    def __init__(self, function_route, entry=None):
        super().__init__()
        self.function_route = function_route
        self.entry = entry
        self.isActive = True
    
    def run(self):
        result = {
            'success': False,
            'message': 'N/A',
            'dictData': {},
            'listData': [],
        }
         
        try:
            with postgres_db:
                if self.function_route == 'loadItem':
                    result = self.loadItem(self.entry, result)
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

    def stop(self):
        self.isActive = False  # Set the flag to stop the thread
        
    # add function here
    def loadItem(self, entry=None, result=None):
        # Load the CSV file using pandas
        if entry['replaceData'] is True:
            itemType = ItemType.delete().execute()
            brand = Brand.delete().execute()
            supplier = Supplier.delete().execute()
            item = Item.delete().execute()
            itemPrice = ItemPrice.delete().execute()
            stock = Stock.delete().execute()

        df = pd.read_csv(entry['filePath'], encoding='utf-8')

        # Define the expected headers
        expectedHeaders = ['ItemName', 'Barcode', 'ExpireDate', 'ItemType', 'Brand', 'Supplier', 
                            'Capital', 'RetailPrice', 'WholesalePrice', 'EffectiveDate']
        
        # Check if the CSV file contains the required headers
        if list(df.columns) != expectedHeaders:
            print("CSV file headers do not match the expected format.")
            return
        
        totalDataCount = len(df)
        
        result['dictData'] = {
            'dataRepresentation': None,
            'currentDataCount': 0,
            'totalDataCount': totalDataCount,
        }
        dictData = result['dictData']
        
        try:
            # Process each row in the DataFrame
            for _, row in df.iterrows():
                if not self.isActive:
                    result['success'] = True
                    result['message'] = 'Loading canceled'
                    return result
                
                itemName = row['ItemName'].upper() if not pd.isna(row['ItemName']) else '_'
                barcode = row['Barcode'] if not pd.isna(row['Barcode']) else '_'
                expireDate = row['ExpireDate'] if not pd.isna(row['ExpireDate']) else datetime.strptime('9999-12-12', '%Y-%m-%d')
                itemTypeName = row['ItemType'].upper() if not pd.isna(row['ItemType']) else '_'
                brandName = row['Brand'].upper() if not pd.isna(row['Brand']) else '_'
                supplierName = row['Supplier'].upper() if not pd.isna(row['Supplier']) else '_'
                capital = row['Capital'] if not pd.isna(row['Capital']) else 0.0
                retailPrice = row['RetailPrice'] if not pd.isna(row['RetailPrice']) else 0.0
                wholesalePrice = row['WholesalePrice'] if not pd.isna(row['WholesalePrice']) else 0.0
                effectiveDate = row['EffectiveDate'] if not pd.isna(row['EffectiveDate']) else datetime.now()

                print('IMPORTING:', itemName, barcode, expireDate, itemTypeName, brandName, supplierName, capital, retailPrice, wholesalePrice, effectiveDate)

                # TODO: write this in a better way by isolating it or something
                itemType = ItemType.select().where(ItemType.ItemTypeName == itemTypeName)
                brand = Brand.select().where(Brand.BrandName == brandName)
                supplier = Supplier.select().where(Supplier.SupplierName == supplierName)
                
                itemType = ItemType.create(ItemTypeName=itemTypeName) if not itemType.exists() else itemType.first()
                brand = Brand.create(BrandName=brandName) if not brand.exists() else brand.first()
                supplier = Supplier.create(SupplierName=supplierName) if not supplier.exists() else supplier.first()
                
                salesGroupEntries = [
                    {'salesGroupName': 'retail'.upper(), 'salesGroupPrice': retailPrice},
                    {'salesGroupName': 'wholesale'.upper(), 'salesGroupPrice': wholesalePrice},
                ]
                
                for salesGroupEntry in salesGroupEntries:
                    item = Item.select().where(
                        (Item.ItemName == itemName) &
                        (Item.Barcode == barcode) &
                        (Item.ExpireDate == expireDate) &
                        (Item.ItemTypeId == itemType.Id) &
                        (Item.BrandId == brand.Id) &
                        (Item.SupplierId == supplier.Id) &
                        (Item.SalesGroupId == SalesGroup.get_or_none(SalesGroup.SalesGroupName == salesGroupEntry['salesGroupName']).Id)
                    )
                    
                    # if item.exists():
                    #     result['message'] = 'Item already exists'
                    #     return result
                    
                    item = Item.create(
                        ItemName=itemName,
                        Barcode=barcode,
                        ExpireDate=expireDate,
                        ItemTypeId=itemType.Id,
                        BrandId=brand.Id,
                        SupplierId=supplier.Id,
                        SalesGroupId=SalesGroup.get_or_none(SalesGroup.SalesGroupName == salesGroupEntry['salesGroupName']).Id,
                    ) if not item.exists() else item.first()
                    
                    itemPrice = ItemPrice.select().where(
                        (ItemPrice.ItemId == item.Id) &
                        (ItemPrice.Price == salesGroupEntry['salesGroupPrice']) & 
                        (ItemPrice.EffectiveDate == effectiveDate) 
                    )
                
                    if itemPrice.exists():
                        continue
                    
                    itemPrice = ItemPrice.create(
                        ItemId=item.Id,
                        Capital=capital,
                        Price=salesGroupEntry['salesGroupPrice'], 
                        EffectiveDate=effectiveDate,
                    )
                    
                dictData['dataRepresentation'] = itemName
                dictData['currentDataCount'] += 1

                self.running.emit(dictData)

            result['success'] = True
            result['message'] = 'Items loaded'
            return result

        except Exception as exception:
            result['success'] = False
            result['message'] = f"An error occured: {exception}"
            return result
        
        