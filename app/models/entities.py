from peewee import *
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

    def __str__(self):
        return self.BrandName

class ItemType(BaseModel):
    Id = AutoField()
    ItemTypeName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'ItemType'

    def __str__(self):
        return self.ItemTypeName

class Organization(BaseModel):
    Id = AutoField()
    TaxId = CharField(max_length=255, null=True)
    OrganizationName = CharField(max_length=255, null=True)
    Address = CharField(max_length=255, null=True)
    MobileNumber = CharField(max_length=20, null=True)
    AccessCode = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Organization'

    def __str__(self):
        return self.OrganizationName

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

    def __str__(self):
        return self.MemberName

class Promo(BaseModel):
    Id = AutoField()
    PromoName = CharField(max_length=255, null=True)
    DiscountRate = FloatField(null=True)
    Description = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Promo'

    def __str__(self):
        return self.PromoName

class Reward(BaseModel):
    Id = AutoField()
    RewardName = CharField(max_length=255, null=True)
    Points = FloatField(null=True)
    Target = FloatField(null=True)
    Description = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Reward'

    def __str__(self):
        return self.RewardName

class SalesGroup(BaseModel):
    Id = AutoField()
    SalesGroupName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'SalesGroup'

    def __str__(self):
        return self.SalesGroupName

class Supplier(BaseModel):
    Id = AutoField()
    SupplierName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Supplier'

    def __str__(self):
        return self.SupplierName
    
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

    def __str__(self):
        return self.ItemName

class ItemPrice(BaseModel):
    Id = AutoField()
    ItemId = ForeignKeyField(Item, on_delete='CASCADE', column_name='ItemId', null=True)
    Capital = FloatField(null=True)
    Price = FloatField(null=True)
    PromoId = ForeignKeyField(Promo, on_delete='CASCADE', column_name='PromoId', null=True)
    Discount = FloatField(null=True)
    EffectiveDate = DateField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'ItemPrice'

    def __str__(self):
        return f"ItemPrice {self.Id}"

class Stock(BaseModel):
    Id = AutoField()
    ItemId = ForeignKeyField(Item, on_delete='CASCADE', column_name='ItemId', null=True)
    OnHand = IntegerField(null=True)
    Available = IntegerField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Stock'

    def __str__(self):
        return f"Stock {self.Id}"
class User(BaseModel):
    Id = AutoField()
    OrganizationId = ForeignKeyField(Organization, on_delete='CASCADE', column_name='OrganizationId', null=True)
    UserName = CharField(max_length=255, null=False)
    AccessCode = CharField(max_length=255, null=False)
    FullName = CharField(max_length=255, null=True)
    BirthDate = DateField(null=True)
    MobileNumber = CharField(max_length=20, null=True)
    AccessLevel = IntegerField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'User'

    def __str__(self):
        return self.UserName

class UserSession(BaseModel):
    Id = AutoField()
    UserId = ForeignKeyField(User, on_delete='CASCADE', column_name='UserId', null=True)
    ActiveStatus = IntegerField(null=True)
    LastLoginTs = DateTimeField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'UserSession'

    def __str__(self):
        return f"UserSessionInfo {self.Id}"

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

    def __str__(self):
        return str(self.DateValue)

class Sale(BaseModel):
    Id = AutoField()
    UserId = ForeignKeyField(User, on_delete='CASCADE', column_name='UserId', null=True)
    CustomerId = ForeignKeyField(Member, on_delete='CASCADE', column_name='CustomerId', null=True)
    ItemId = ForeignKeyField(Item, on_delete='CASCADE', column_name='ItemId', null=True)
    Quantity = IntegerField(null=True)
    QuantityPrice = FloatField(null=True)
    Reason = TextField(null=True)
    ReferenceId = CharField(max_length=255, null=True)
    Status = IntegerField(null=True)
    DateId = ForeignKeyField(Date, on_delete='CASCADE', column_name='DateId', null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Sale'

    def __str__(self):
        return f"Sale {self.Id}"
