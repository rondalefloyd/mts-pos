import os, sys
from sqlalchemy.orm import sessionmaker, registry

sys.path.append(os.path.abspath(''))
from app.models.system import (
    user,
    organization,
    configuration
)
from app.models.sales import (
    item,
    itemPrice,
    brand,
    itemType,
    salesGroup,
    supplier,
    promo,
    stock,
)

class User:
    def __init__(self):
        print('initializing User object...')
        
class Organization:
    def __init__(self):
        print('initializing Organization object...')
    
class Configuration:
    def __init__(self):
        print('initializing Configuration object...')
                  
class Item:
    def __init__(self):
        print('initializing Item object...')
            
class ItemPrice:
    def __init__(self):
        print('initializing ItemPrice object...')
            
class Brand:
    def __init__(self):
        print('initializing Brand object...')
            
class ItemType:
    def __init__(self):
        print('initializing ItemType object...')
            
class SalesGroup:
    def __init__(self):
        print('initializing SalesGroup object...')
            
class Supplier:
    def __init__(self):
        print('initializing Supplier object...')
            
class Promo:
    def __init__(self):
        print('initializing Promo object...')

class Stock:
    def __init__(self):
        print('initializing Stock object...')

# Map the classes to the existing tables
registry().map_imperatively(User, user)
registry().map_imperatively(Organization, organization)
registry().map_imperatively(Configuration, configuration)
registry().map_imperatively(Item, item)
registry().map_imperatively(ItemPrice, itemPrice)
registry().map_imperatively(Brand, brand)
registry().map_imperatively(ItemType, itemType)
registry().map_imperatively(SalesGroup, salesGroup)
registry().map_imperatively(Supplier, supplier)
registry().map_imperatively(Promo, promo)
registry().map_imperatively(Stock, stock)

