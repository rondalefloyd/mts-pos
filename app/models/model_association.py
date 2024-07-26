import os
import sys
from peewee import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.utils.database import postgres_db

class BaseModel(Model):
    class Meta:
        database = postgres_db

class Brand(BaseModel):
    BrandId = AutoField()
    BrandName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        table_name = 'Brand'

class Item(BaseModel):
    ItemId = AutoField()
    ItemName = CharField(max_length=255, null=True)
    Barcode = CharField(max_length=255, null=True)
    ExpireDate = DateField(null=True)
    ItemTypeId = IntegerField(null=True)
    BrandId = IntegerField(null=True)
    SalesGroupId = IntegerField(null=True)
    SupplierId = IntegerField(null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        table_name = 'Item'

class ItemPrice(BaseModel):
    ItemPriceId = AutoField()
    ItemId = IntegerField(null=True)
    Capital = FloatField(null=True)
    Price = FloatField(null=True)
    PromoId = IntegerField(null=True)
    Discount = FloatField(null=True)
    EffectiveDate = DateField(null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        table_name = 'ItemPrice'

class ItemType(BaseModel):
    ItemTypeId = AutoField()
    ItemTypeName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        table_name = 'ItemType'

class Member(BaseModel):
    Id = AutoField()
    OrganizationId = IntegerField(null=True)
    MemberName = CharField(max_length=255, null=True)
    BirthDate = DateField(null=True)
    Address = CharField(max_length=255, null=True)
    MobileNumber = CharField(max_length=20, null=True)
    Points = FloatField(null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        table_name = 'Member'

class Organization(BaseModel):
    Id = AutoField()
    TaxId = CharField(max_length=255, null=True)
    OrganizationName = CharField(max_length=255, null=True)
    Address = CharField(max_length=255, null=True)
    MobileNumber = CharField(max_length=20, null=True)
    AccessCode = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        table_name = 'Organization'

class Promo(BaseModel):
    PromoId = AutoField()
    PromoName = CharField(max_length=255, null=True)
    DiscountRate = FloatField(null=True)
    Description = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        table_name = 'Promo'

class SalesGroup(BaseModel):
    SalesGroupId = AutoField()
    SalesGroupName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        table_name = 'SalesGroup'

class Stock(BaseModel):
    StockId = AutoField()
    ItemId = IntegerField(null=True)
    OnHand = IntegerField(null=True)
    Available = IntegerField(null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        table_name = 'Stock'

class Supplier(BaseModel):
    SupplierId = AutoField()
    SupplierName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        table_name = 'Supplier'

class User(BaseModel):
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
        table_name = 'User'
