from peewee import *
from app.utils.database import postgres_db

class BaseModel(Model):
    class Meta:
        database = postgres_db

class Brand(BaseModel):
    BrandId = AutoField()
    BrandName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Brand'  # Explicitly specify the table name

    def __str__(self):
        return self.BrandName

class Item(BaseModel):
    ItemId = AutoField()
    ItemName = CharField(max_length=255, null=True)
    Barcode = CharField(max_length=255, null=True)
    ExpireDate = DateField(null=True)
    ItemTypeId = IntegerField(null=True)
    BrandId = IntegerField(null=True)
    SalesGroupId = IntegerField(null=True)
    SupplierId = IntegerField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Item'  # Explicitly specify the table name

    def __str__(self):
        return self.ItemName

class ItemPrice(BaseModel):
    ItemPriceId = AutoField()
    ItemId = IntegerField(null=True)
    Capital = FloatField(null=True)
    Price = FloatField(null=True)
    PromoId = IntegerField(null=True)
    Discount = FloatField(null=True)
    EffectiveDate = DateField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'ItemPrice'  # Explicitly specify the table name

    def __str__(self):
        return f"ItemPrice {self.ItemPriceId}"

class ItemType(BaseModel):
    ItemTypeId = AutoField()
    ItemTypeName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'ItemType'  # Explicitly specify the table name

    def __str__(self):
        return self.ItemTypeName

class Member(BaseModel):
    Id = AutoField()
    OrganizationId = IntegerField(null=True)
    MemberName = CharField(max_length=255, null=True)
    BirthDate = DateField(null=True)
    Address = CharField(max_length=255, null=True)
    MobileNumber = CharField(max_length=20, null=True)
    Points = FloatField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Member'  # Explicitly specify the table name

    def __str__(self):
        return self.MemberName

class Organization(BaseModel):
    Id = AutoField()
    TaxId = CharField(max_length=255, null=True)
    OrganizationName = CharField(max_length=255, null=True)
    Address = CharField(max_length=255, null=True)
    MobileNumber = CharField(max_length=20, null=True)
    AccessCode = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Organization'  # Explicitly specify the table name

    def __str__(self):
        return self.OrganizationName

class Promo(BaseModel):
    PromoId = AutoField()
    PromoName = CharField(max_length=255, null=True)
    DiscountRate = FloatField(null=True)
    Description = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Promo'  # Explicitly specify the table name

    def __str__(self):
        return self.PromoName

class SalesGroup(BaseModel):
    SalesGroupId = AutoField()
    SalesGroupName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'SalesGroup'  # Explicitly specify the table name

    def __str__(self):
        return self.SalesGroupName

class Stock(BaseModel):
    StockId = AutoField()
    ItemId = IntegerField(null=True)
    OnHand = IntegerField(null=True)
    Available = IntegerField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Stock'  # Explicitly specify the table name

    def __str__(self):
        return f"Stock {self.StockId}"

class Supplier(BaseModel):
    SupplierId = AutoField()
    SupplierName = CharField(max_length=255, null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'Supplier'  # Explicitly specify the table name

    def __str__(self):
        return self.SupplierName

class User(BaseModel):
    Id = AutoField()
    OrganizationId = IntegerField(null=True)
    UserName = CharField(max_length=255, null=False)
    AccessCode = CharField(max_length=255, null=False)
    FullName = CharField(max_length=255, null=True)
    BirthDate = DateField(null=True)
    MobileNumber = CharField(max_length=20, null=True)
    AccessLevel = IntegerField(null=True)
    ActiveStatus = BooleanField(default=True)
    LastLoginTs = DateTimeField(null=True)
    LastLogoutTs = DateTimeField(null=True)
    UpdateTs = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], null=True)

    class Meta:
        table_name = 'User'  # Explicitly specify the table name

    def __str__(self):
        return self.UserName
