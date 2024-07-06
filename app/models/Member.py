from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Float,
)
from datetime import datetime

def memberTable(metadata):
    member = Table('Member', metadata,
        Column('Id', Integer, primary_key=True, autoincrement=True),
        Column('OrganizationId', Integer, default=None),
        Column('MemberName', String, default=None),
        Column('BirthDate', String, default=None),
        Column('Address', String, default=None),
        Column('MobileNumber', String, default=None),
        Column('Points', Float, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )
    
    return member