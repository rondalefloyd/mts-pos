import os, sys
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import registry, sessionmaker
from datetime import datetime

sys.path.append(os.path.abspath(''))
from app.models.Authentication import authenticationTable
from app.models.Brand import brandTable
from app.models.Item import itemTable
from app.models.ItemPrice import itemPriceTable
from app.models.ItemType import itemTypeTable
from app.models.Member import memberTable
from app.models.Organization import organizationTable
from app.models.Promo import promoTable
from app.models.SalesGroup import salesGroupTable
from app.models.Stock import stockTable
from app.models.Supplier import supplierTable
from app.models.User import userTable

engine = None
status = 'OFFLINE'
metadata = MetaData()
currentDateTime = datetime.now()
onlineUrl = f"{os.getenv('ONLINE_SQLALCHEMY_BASE_URL')}://{os.getenv('TURSO_DB_URL')}/?authToken={os.getenv('TURSO_DB_AUTH_TOKEN')}"
offlineUrl = f"{os.getenv('OFFLINE_SQLALCHEMY_BASE_URL')}:///{os.getenv('OFFLINE_DB_FILE_PATH')}/pos.db"
table = {
    'authentication': authenticationTable(metadata),
    'brand': brandTable(metadata),
    'item': itemTable(metadata),
    'itemPrice': itemPriceTable(metadata),
    'itemType': itemTypeTable(metadata),
    'member': memberTable(metadata),
    'organization': organizationTable(metadata),
    'promo': promoTable(metadata),
    'salesGroup': salesGroupTable(metadata),
    'stock': stockTable(metadata),
    'supplier': supplierTable(metadata),
    'user': userTable(metadata),
}

while status == 'OFFLINE':
    try:
        print(onlineUrl)
        engine = create_engine(
            url = onlineUrl, 
            connect_args = {'check_same_thread': False}, 
            echo = True
        )
        
        metadata.create_all(bind=engine)
        status = 'ONLINE'

    except Exception as error:
        print('Error:', error)
        print('Switching to local database...')
        print(offlineUrl)

        engine = create_engine(
            url = offlineUrl, 
            connect_args = {'check_same_thread': False}, 
            echo = True
        )
        
        metadata.create_all(bind=engine)
    
session = sessionmaker(bind=engine)()

# Define the classes in the same order as the table functions are imported
class Authentication:
    def __init__(self):
        print('initializing Authentication object...')

class Brand:
    def __init__(self):
        print('initializing Brand object...')

class Item:
    def __init__(self):
        print('initializing Item object...')

class ItemPrice:
    def __init__(self):
        print('initializing ItemPrice object...')

class ItemType:
    def __init__(self):
        print('initializing ItemType object...')

class Member:
    def __init__(self):
        print('initializing Member object...')

class Organization:
    def __init__(self):
        print('initializing Organization object...')

class Promo:
    def __init__(self):
        print('initializing Promo object...')

class SalesGroup:
    def __init__(self):
        print('initializing SalesGroup object...')

class Stock:
    def __init__(self):
        print('initializing Stock object...')

class Supplier:
    def __init__(self):
        print('initializing Supplier object...')

class User:
    def __init__(self):
        print('initializing User object...')

# Map the classes to the existing tables
registry().map_imperatively(Authentication, table['authentication'])
registry().map_imperatively(Brand, table['brand'])
registry().map_imperatively(Item, table['item'])
registry().map_imperatively(ItemPrice, table['itemPrice'])
registry().map_imperatively(ItemType, table['itemType'])
registry().map_imperatively(Member, table['member'])
registry().map_imperatively(Organization, table['organization'])
registry().map_imperatively(Promo, table['promo'])
registry().map_imperatively(SalesGroup, table['salesGroup'])
registry().map_imperatively(Stock, table['stock'])
registry().map_imperatively(Supplier, table['supplier'])
registry().map_imperatively(User, table['user'])