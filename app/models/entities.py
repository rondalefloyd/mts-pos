from peewee import *
from app.utils.databases import postgres_db

class BaseModel(Model):
    class Meta:
        database = postgres_db

class Brands(BaseModel):
    Id = AutoField()
    BrandName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Brands'

    def __str__(self):
        return self.BrandName

class ItemTypes(BaseModel):
    Id = AutoField()
    ItemTypeName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'ItemTypes'

    def __str__(self):
        return self.ItemTypeName

class Organizations(BaseModel):
    Id = AutoField()
    TaxId = CharField(max_length=255, null=True)
    OrganizationName = CharField(max_length=255, null=True)
    Address = CharField(max_length=255, null=True)
    MobileNumber = CharField(max_length=20, null=True)
    AccessCode = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Organizations'

    def __str__(self):
        return self.OrganizationName

class Members(BaseModel):
    Id = AutoField()
    OrganizationId = ForeignKeyField(Organizations, on_delete='CASCADE', column_name='OrganizationId', null=True)
    MemberName = CharField(max_length=255, null=True)
    BirthDate = DateField(null=True)
    Address = CharField(max_length=255, null=True)
    MobileNumber = CharField(max_length=20, null=True)
    Points = FloatField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Members'

    def __str__(self):
        return self.MemberName

class Promos(BaseModel):
    Id = AutoField()
    PromoName = CharField(max_length=255, null=True)
    DiscountRate = FloatField(null=True)
    Description = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Promos'

    def __str__(self):
        return self.PromoName

class Rewards(BaseModel):
    Id = AutoField()
    RewardName = CharField(max_length=255, null=True)
    Points = FloatField(null=True)
    Target = FloatField(null=True)
    Description = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Rewards'

    def __str__(self):
        return self.RewardName

class SalesGroups(BaseModel):
    Id = AutoField()
    SalesGroupName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'SalesGroups'

    def __str__(self):
        return self.SalesGroupName

class Suppliers(BaseModel):
    Id = AutoField()
    SupplierName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Suppliers'

    def __str__(self):
        return self.SupplierName
    
class Items(BaseModel):
    Id = AutoField()
    ItemName = CharField(max_length=255, null=True)
    Barcode = CharField(max_length=255, null=True)
    ExpireDate = DateField(null=True)
    ItemTypeId = ForeignKeyField(ItemTypes, on_delete='CASCADE', column_name='ItemTypeId', null=True)
    BrandId = ForeignKeyField(Brands, on_delete='CASCADE', column_name='BrandId', null=True)
    SalesGroupId = ForeignKeyField(SalesGroups, on_delete='CASCADE', column_name='SalesGroupId', null=True)
    SupplierId = ForeignKeyField(Suppliers, on_delete='CASCADE', column_name='SupplierId', null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Items'

    def __str__(self):
        return self.ItemName

class ItemPrices(BaseModel):
    Id = AutoField()
    ItemId = ForeignKeyField(Items, on_delete='CASCADE', column_name='ItemId', null=True)
    Capital = FloatField(null=True)
    Price = FloatField(null=True)
    PromoId = ForeignKeyField(Promos, on_delete='CASCADE', column_name='PromoId', null=True)
    Discount = FloatField(null=True)
    EffectiveDate = DateField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'ItemPrices'

    def __str__(self):
        return f"ItemPrice {self.Id}"

class Stocks(BaseModel):
    Id = AutoField()
    ItemId = ForeignKeyField(Items, on_delete='CASCADE', column_name='ItemId', null=True)
    OnHand = IntegerField(null=True)
    Available = IntegerField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Stocks'

    def __str__(self):
        return f"Stock {self.Id}"
class Users(BaseModel):
    Id = AutoField()
    OrganizationId = ForeignKeyField(Organizations, on_delete='CASCADE', column_name='OrganizationId', null=True)
    UserName = CharField(max_length=255, null=False)
    AccessCode = CharField(max_length=255, null=False)
    FullName = CharField(max_length=255, null=True)
    BirthDate = DateField(null=True)
    MobileNumber = CharField(max_length=20, null=True)
    AccessLevel = IntegerField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Users'

    def __str__(self):
        return self.UserName

class UserSessionInfos(BaseModel):
    Id = AutoField()
    UserId = ForeignKeyField(Users, on_delete='CASCADE', column_name='UserId', null=True)
    ActiveStatus = IntegerField(null=True)
    LastLoginTs = DateTimeField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'UserSessionInfos'

    def __str__(self):
        return f"UserSessionInfo {self.Id}"

class Dates(BaseModel):
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
        table_name = 'Dates'

    def __str__(self):
        return str(self.DateValue)

class Sales(BaseModel):
    Id = AutoField()
    UserId = ForeignKeyField(Users, on_delete='CASCADE', column_name='UserId', null=True)
    CustomerId = ForeignKeyField(Members, on_delete='CASCADE', column_name='CustomerId', null=True)
    ItemId = ForeignKeyField(Items, on_delete='CASCADE', column_name='ItemId', null=True)
    Quantity = IntegerField(null=True)
    QuantityPrice = FloatField(null=True)
    Reason = TextField(null=True)
    ReferenceId = CharField(max_length=255, null=True)
    Status = IntegerField(null=True)
    DateId = ForeignKeyField(Dates, on_delete='CASCADE', column_name='DateId', null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Sales'

    def __str__(self):
        return f"Sale {self.Id}"
