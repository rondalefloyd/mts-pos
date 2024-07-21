from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Float,
)
from datetime import datetime

def itemTable(metadata):
    item = Table('Item', metadata,
        Column('ItemId', Integer, primary_key=True, autoincrement=True),
        Column('ItemName', String, default=None),
        Column('Barcode', String, default=None),
        Column('ExpireDate', String, default=None),
        Column('ItemTypeId', Integer, default=None),
        Column('BrandId', Integer, default=None),
        Column('SalesGroupId', Integer, default=None),
        Column('SupplierId', Integer, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )

    return item