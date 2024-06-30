import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

engine = create_engine(f'sqlite:///{os.path.abspath('tests\\database\\sales.db')}', echo=True)
metadata = MetaData()
session = sessionmaker(bind=engine)()


item = Table('Item', metadata,
    Column('ItemId', Integer, primary_key=True, autoincrement=True),
    Column('ItemName', String, default=None),
    Column('Barcode', String, default=None),
    Column('ExpireDate', String, default=None),
    Column('ItemTypeId', Integer, default=None),
    Column('BrandId', Integer, default=None),
    Column('SalesGroupId', Integer, default=None),
    Column('SupplierId', Integer, default=None),
    Column('UpdateTs', String, server_default=func.now()),
)

itemPrice = Table('ItemPrice', metadata,
    Column('ItemPriceId', Integer, primary_key=True, autoincrement=True),
    Column('ItemId', Integer, default=None),
    Column('Capital', Float, default=None),
    Column('Price', Float, default=None),
    Column('PromoId', Integer, default=None),
    Column('Discount', Float, default=None),
    Column('EffectiveDate', String, default=None),
    Column('UpdateTs', String, server_default=func.now()),
)

brand = Table('Brand', metadata,
    Column('BrandId', Integer, primary_key=True, autoincrement=True),
    Column('BrandName', String, default=None),
    Column('UpdateTs', String, server_default=func.now()),
)

itemType = Table('ItemType', metadata,
    Column('ItemTypeId', Integer, primary_key=True, autoincrement=True),
    Column('ItemTypeName', String, default=None),
    Column('UpdateTs', String, server_default=func.now()),
)

salesGroup = Table('SalesGroup', metadata,
    Column('SalesGroupId', Integer, primary_key=True, autoincrement=True),
    Column('SalesGroupName', String, default=None),
    Column('UpdateTs', String, server_default=func.now()),
)

supplier = Table('Supplier', metadata,
    Column('SupplierId', Integer, primary_key=True, autoincrement=True),
    Column('SupplierName', String, default=None),
    Column('UpdateTs', String, server_default=func.now()),
)

promo = Table('Promo', metadata,
    Column('PromoId', Integer, primary_key=True, autoincrement=True),
    Column('PromoName', String, default=None),
    Column('DiscountRate', Float, default=None),
    Column('Description', String, default=None),
    Column('UpdateTs', String, server_default=func.now()),
)

stock = Table('Stock', metadata,
    Column('StockId', Integer, primary_key=True, autoincrement=True),
    Column('ItemId', Float, default=None),
    Column('OnHand', Integer, default=None),
    Column('Available', Integer, default=None),
    Column('UpdateTs', String, server_default=func.now()),
)

metadata.reflect(bind=engine)