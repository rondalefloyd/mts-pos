import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(
    url = f"sqlite+{os.getenv('TURSO_DB_URL')}/?authToken={os.getenv('TURSO_DB_AUTH_TOKEN')}", 
    connect_args = {'check_same_thread': False}, 
    echo = True
)

print(f"sqlite+{os.getenv('TURSO_DB_URL')}/?authToken={os.getenv('TURSO_DB_AUTH_TOKEN')}")

# engine = create_engine(f'sqlite:///{os.getenv('DATABASE_FILE_PATH')}', echo=True)
metadata = MetaData()
session = sessionmaker(bind=engine)()

user = Table('User', metadata,
    Column('UserId', Integer, primary_key=True, autoincrement=True),
    Column('FullName', String, default=None),
    Column('BirthDate', String, default=None),
    Column('MobileNumber', String, default=None),
    Column('UserName', String, default=None),
    Column('AccessCode', String, default=None),
    Column('AccessLevel', Integer, default=None),
    Column('OrganizationId', Integer, default=None),
    Column('UpdateTs', String, server_default=func.now()),
)

organization = Table('Organization', metadata,
    Column('OrganizationId', Integer, primary_key=True, autoincrement=True),
    Column('OrganizationName', String, default=None),
    Column('Address', String, default=None),
    Column('MobileNumber', String, default=None),
    Column('TaxId', String, default=None),
    Column('AccessCode', String, default=None),
    Column('UpdateTs', String, server_default=func.now()),
)

configuration = Table('Configuration', metadata,
    Column('ConfigurationId', Integer, primary_key=True, autoincrement=True),
    Column('MachineId', String, default=None),
    Column('LastLoginUserName', String, default=None),
    Column('LastLoginAccessCode', String, default=None),
    Column('IsRememberUser', String, default=None),
    Column('UpdateTs', String, server_default=func.now()),
)

metadata.reflect(bind=engine)