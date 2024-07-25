import os, sys
from peewee import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.utils.database import db

class User(Model):
    Id = AutoField()
    OrganizationId = IntegerField(null=True)
    UserName = CharField(max_length=255, null=True)
    AccessCode = CharField(max_length=255, null=True)
    FullName = CharField(max_length=255, null=True)
    BirthDate = DateField(null=True)
    MobileNumber = CharField(max_length=20, null=True)
    AccessLevel = IntegerField(null=True)
    ActiveStatus = IntegerField(null=True)
    LastLoginTs = DateTimeField(null=True)
    LastLogoutTs = DateTimeField(null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = 'User'
