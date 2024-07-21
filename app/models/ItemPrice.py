from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Float,
)
from datetime import datetime

def itemPriceTable(metadata):
    itemPrice = Table('ItemPrice', metadata,
        Column('ItemPriceId', Integer, primary_key=True, autoincrement=True),
        Column('ItemId', Integer, default=None),
        Column('Capital', Float, default=None),
        Column('Price', Float, default=None),
        Column('PromoId', Integer, default=None),
        Column('Discount', Float, default=None),
        Column('EffectiveDate', String, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )
    return itemPrice