from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
)
from datetime import datetime

def salesGroupTable(metadata):
    salesGroup = Table('SalesGroup', metadata,
        Column('SalesGroupId', Integer, primary_key=True, autoincrement=True),
        Column('SalesGroupName', String, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )

    return salesGroup