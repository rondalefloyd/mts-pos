CREATE TABLE "Brand" (
    "BrandId" SERIAL PRIMARY KEY, 
    "BrandName" VARCHAR(255), 
    "UpdateTs" TIMESTAMP
);

CREATE TABLE "Item" (
    "ItemId" SERIAL PRIMARY KEY, 
    "ItemName" VARCHAR(255), 
    "Barcode" VARCHAR(255), 
    "ExpireDate" DATE, 
    "ItemTypeId" INTEGER, 
    "BrandId" INTEGER, 
    "SalesGroupId" INTEGER, 
    "SupplierId" INTEGER, 
    "UpdateTs" TIMESTAMP
);

CREATE TABLE "ItemPrice" (
    "ItemPriceId" SERIAL PRIMARY KEY, 
    "ItemId" INTEGER, 
    "Capital" FLOAT, 
    "Price" FLOAT, 
    "PromoId" INTEGER, 
    "Discount" FLOAT, 
    "EffectiveDate" DATE, 
    "UpdateTs" TIMESTAMP
);

CREATE TABLE "ItemType" (
    "ItemTypeId" SERIAL PRIMARY KEY, 
    "ItemTypeName" VARCHAR(255), 
    "UpdateTs" TIMESTAMP
);

CREATE TABLE "Member" (
    "Id" SERIAL PRIMARY KEY, 
    "OrganizationId" INTEGER, 
    "MemberName" VARCHAR(255), 
    "BirthDate" DATE, 
    "Address" VARCHAR(255), 
    "MobileNumber" VARCHAR(20), 
    "Points" FLOAT, 
    "UpdateTs" TIMESTAMP
);

CREATE TABLE "Organization" (
    "Id" SERIAL PRIMARY KEY, 
    "TaxId" VARCHAR(255), 
    "OrganizationName" VARCHAR(255), 
    "Address" VARCHAR(255), 
    "MobileNumber" VARCHAR(20), 
    "AccessCode" VARCHAR(255), 
    "UpdateTs" TIMESTAMP
);

CREATE TABLE "Promo" (
    "PromoId" SERIAL PRIMARY KEY, 
    "PromoName" VARCHAR(255), 
    "DiscountRate" FLOAT, 
    "Description" VARCHAR(255), 
    "UpdateTs" TIMESTAMP
);

CREATE TABLE "SalesGroup" (
    "SalesGroupId" SERIAL PRIMARY KEY, 
    "SalesGroupName" VARCHAR(255), 
    "UpdateTs" TIMESTAMP
);

CREATE TABLE "Stock" (
    "StockId" SERIAL PRIMARY KEY, 
    "ItemId" INTEGER, 
    "OnHand" INTEGER, 
    "Available" INTEGER, 
    "UpdateTs" TIMESTAMP
);

CREATE TABLE "Supplier" (
    "SupplierId" SERIAL PRIMARY KEY, 
    "SupplierName" VARCHAR(255), 
    "UpdateTs" TIMESTAMP
);

CREATE TABLE "User" (
    "Id" SERIAL PRIMARY KEY, 
    "OrganizationId" INTEGER, 
    "UserName" VARCHAR(255), 
    "AccessCode" VARCHAR(255), 
    "FullName" VARCHAR(255), 
    "BirthDate" DATE, 
    "MobileNumber" VARCHAR(20), 
    "AccessLevel" INTEGER, 
    "ActiveStatus" INTEGER, 
    "LastLoginTs" TIMESTAMP, 
    "LastLogoutTs" TIMESTAMP, 
    "UpdateTs" TIMESTAMP
);
