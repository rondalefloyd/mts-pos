from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
)
from datetime import datetime

def itemTypeTable(metadata):
    itemType = Table('ItemType', metadata,
        Column('ItemTypeId', Integer, primary_key=True, autoincrement=True),
        Column('ItemTypeName', String, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )
    
    return itemType