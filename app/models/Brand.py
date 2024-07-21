from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
)
from datetime import datetime

def brandTable(metadata):
    brand = Table('Brand', metadata,
        Column('BrandId', Integer, primary_key=True, autoincrement=True),
        Column('BrandName', String, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )
    
    return brand