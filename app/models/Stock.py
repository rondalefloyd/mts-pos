from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
)
from datetime import datetime

def stockTable(metadata):
    stock = Table('Stock', metadata,
        Column('StockId', Integer, primary_key=True, autoincrement=True),
        Column('ItemId', Integer, default=None),
        Column('OnHand', Integer, default=None),
        Column('Available', Integer, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )

    return stock