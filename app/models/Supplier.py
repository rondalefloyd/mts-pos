from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
)
from datetime import datetime

def supplierTable(metadata):
    supplier = Table('Supplier', metadata,
        Column('SupplierId', Integer, primary_key=True, autoincrement=True),
        Column('SupplierName', String, default=None),
        Column('UpdateTs', String, default=datetime.now()),
    )

    return supplier