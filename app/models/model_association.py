import os, sys
from sqlalchemy import MetaData
from sqlalchemy.orm import registry

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
metadata = MetaData()

registry().map_imperatively(Authentication, authenticationTable(metadata))
registry().map_imperatively(Brand, brandTable(metadata))
registry().map_imperatively(Item, itemTable(metadata))
registry().map_imperatively(ItemPrice, itemPriceTable(metadata))
registry().map_imperatively(ItemType, itemTypeTable(metadata))
registry().map_imperatively(Member, memberTable(metadata))
registry().map_imperatively(Organization, organizationTable(metadata))
registry().map_imperatively(Promo, promoTable(metadata))
registry().map_imperatively(SalesGroup, salesGroupTable(metadata))
registry().map_imperatively(Stock, stockTable(metadata))
registry().map_imperatively(Supplier, supplierTable(metadata))
registry().map_imperatively(User, userTable(metadata))