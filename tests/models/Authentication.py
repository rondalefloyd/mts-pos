from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
)
from datetime import datetime

def authenticationTable(metadata):
    authentication = Table('Authentication', metadata,
        Column('Id', Integer, primary_key=True, autoincrement=True),
        Column('MachineId', String, default=None),
        Column('OrganizationId', String, default=None),
        Column('UserId', String, default=None),
        Column('UserName', String, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )
    
    return authentication