from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
)
from datetime import datetime

def organizationTable(metadata):
    organization = Table('Organization', metadata,
        Column('Id', Integer, primary_key=True, autoincrement=True),
        Column('TaxId', String, default=None),
        Column('OrganizationName', String, default=None),
        Column('Address', String, default=None),
        Column('MobileNumber', String, default=None),
        Column('AccessCode', String, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )

    return organization