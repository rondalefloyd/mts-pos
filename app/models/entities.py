from peewee import *
from playhouse.postgres_ext import JSONField
from app.utils.databases import postgres_db

class BaseModel(Model):
    class Meta:
        database = postgres_db

class Brand(BaseModel):
    Id = AutoField()
    BrandName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Brand'

class ItemType(BaseModel):
    Id = AutoField()
    ItemTypeName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'ItemType'

class Organization(BaseModel):
    Id = AutoField()
    TaxId = CharField(max_length=255, null=True)
    OrganizationName = CharField(max_length=255, null=True)
    Address = CharField(max_length=255, null=True)
    MobileNumber = CharField(max_length=20, null=True)
    Password = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Organization'

class Member(BaseModel):
    Id = AutoField()
    OrganizationId = ForeignKeyField(Organization, on_delete='CASCADE', column_name='OrganizationId', null=True)
    MemberName = CharField(max_length=255, null=True)
    BirthDate = DateField(null=True)
    Address = CharField(max_length=255, null=True)
    MobileNumber = CharField(max_length=20, null=True)
    Points = FloatField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Member'

class Promo(BaseModel):
    Id = AutoField()
    PromoName = CharField(max_length=255, null=True)
    DiscountRate = FloatField(null=True)
    Description = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Promo'

class Reward(BaseModel):
    Id = AutoField()
    RewardName = CharField(max_length=255, null=True)
    Points = FloatField(null=True)
    Target = FloatField(null=True)
    Description = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Reward'

class SalesGroup(BaseModel):
    Id = AutoField()
    SalesGroupName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'SalesGroup'

class Supplier(BaseModel):
    Id = AutoField()
    SupplierName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Supplier'

class Item(BaseModel):
    Id = AutoField()
    ItemName = CharField(max_length=255, null=True)
    Barcode = CharField(max_length=255, null=True)
    ExpireDate = DateField(null=True)
    ItemTypeId = ForeignKeyField(ItemType, on_delete='CASCADE', column_name='ItemTypeId', null=True)
    BrandId = ForeignKeyField(Brand, on_delete='CASCADE', column_name='BrandId', null=True)
    SalesGroupId = ForeignKeyField(SalesGroup, on_delete='CASCADE', column_name='SalesGroupId', null=True)
    SupplierId = ForeignKeyField(Supplier, on_delete='CASCADE', column_name='SupplierId', null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Item'

class ItemPrice(BaseModel):
    Id = AutoField()
    ItemId = ForeignKeyField(Item, on_delete='CASCADE', column_name='ItemId', null=True)
    Cost = FloatField(null=True)
    Price = FloatField(null=True)
    PromoId = ForeignKeyField(Promo, on_delete='CASCADE', column_name='PromoId', null=True)
    Discount = FloatField(null=True)
    EffectiveDate = DateField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'ItemPrice'

class Stock(BaseModel):
    Id = AutoField()
    ItemId = ForeignKeyField(Item, on_delete='CASCADE', column_name='ItemId', null=True)
    OnHand = IntegerField(default=0, null=True)
    Available = IntegerField(default=0, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Stock'

class User(BaseModel):
    Id = AutoField()
    OrganizationId = ForeignKeyField(Organization, on_delete='CASCADE', column_name='OrganizationId', null=True)
    UserName = CharField(max_length=255, null=False)
    Password = CharField(max_length=255, null=False)
    FullName = CharField(max_length=255, null=True)
    BirthDate = DateField(null=True)
    MobileNumber = CharField(max_length=20, null=True)
    AccessLevel = IntegerField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'User'

class UserSession(BaseModel):
    Id = AutoField()
    UserId = ForeignKeyField(User, on_delete='CASCADE', column_name='UserId', null=True)
    ActiveStatus = IntegerField(null=True)
    LastLoginTs = DateTimeField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'UserSession'

class Date(BaseModel):
    Id = AutoField()
    DateValue = DateField(unique=True, null=False)
    Dayofweek = IntegerField(null=False)
    Weekday = CharField(max_length=255, null=False)
    Quarter = IntegerField(null=False)
    Year = IntegerField(null=False)
    Month = IntegerField(null=False)
    MonthName = CharField(max_length=255, null=False)
    Day = IntegerField(null=False)
    IsHoliday = BooleanField(constraints=[SQL('DEFAULT FALSE')], null=False)

    class Meta:
        table_name = 'Date'

class OrderType(BaseModel):
    Id = AutoField()
    OrderTypeName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'OrderType'

class Receipt(BaseModel):
    Id = AutoField()
    OrganizationId = ForeignKeyField(Organization, on_delete='CASCADE', column_name='OrganizationId', null=True)
    UserId = ForeignKeyField(User, on_delete='CASCADE', column_name='UserId', null=True)
    MemberId = ForeignKeyField(Member, on_delete='CASCADE', column_name='MemberId', null=True)
    DateId = ForeignKeyField(Date, on_delete='CASCADE', column_name='DateId', null=True)
    OrderTypeId = ForeignKeyField(OrderType, on_delete='CASCADE', column_name='OrderTypeId', null=True)
    ReferenceId = CharField(max_length=255, null=True)
    MachineId = CharField(max_length=255, null=True)
    OrderName = CharField(max_length=255, null=True)
    Billing = JSONField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Receipt'

class ItemSold(BaseModel):
    Id = AutoField()
    ReceiptId = ForeignKeyField(Receipt, on_delete='CASCADE', column_name='ReceiptId', null=True)
    ItemPriceId = ForeignKeyField(Item, on_delete='CASCADE', column_name='ItemPriceId', null=True)
    DateId = ForeignKeyField(Date, on_delete='CASCADE', column_name='DateId', null=True)
    UserId = ForeignKeyField(User, on_delete='CASCADE', column_name='UserId', null=True)
    MemberId = ForeignKeyField(Member, on_delete='CASCADE', column_name='MemberId', null=True)
    Quantity = IntegerField(null=True)
    Total = FloatField(null=True)
    VoidReason = CharField(max_length=255, null=True)
    VoidStatus = IntegerField(null=True)
    StockBypass = IntegerField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'ItemSold'

class POSConfig(BaseModel):
    Id = AutoField()
    OrganizationId = ForeignKeyField(Organization, on_delete='CASCADE', column_name='OrganizationId', null=True)
    Config = JSONField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'POSConfig'

# Ensure to create the tables in the database
def create_tables():
    with postgres_db:
        postgres_db.create_tables([Brand, ItemType, Organization, Member, Promo, Reward, SalesGroup, Supplier, Item, ItemPrice, Stock, User, UserSession, Date, OrderType, Receipt, ItemSold, POSConfig])

if __name__ == '__main__':
    create_tables()