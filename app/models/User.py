from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
)
from datetime import datetime

def userTable(metadata):
    user = Table('User', metadata,
        Column('Id', Integer, primary_key=True, autoincrement=True),
        Column('OrganizationId', Integer, default=None),
        Column('UserName', String, default=None),
        Column('AccessCode', String, default=None),
        Column('FullName', String, default=None),
        Column('BirthDate', String, default=None),
        Column('MobileNumber', String, default=None),
        Column('AccessLevel', Integer, default=None),
        Column('ActiveStatus', Integer, default=None),
        Column('LastLoginTs', String, default=None),
        Column('LastLogoutTs', String, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )

    return user