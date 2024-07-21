from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Float,
)
from datetime import datetime

def promoTable(metadata):
    promo = Table('Promo', metadata,
        Column('PromoId', Integer, primary_key=True, autoincrement=True),
        Column('PromoName', String, default=None),
        Column('DiscountRate', Float, default=None),
        Column('Description', String, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )

    return promo