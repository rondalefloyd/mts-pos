-- Create the Date table
CREATE TABLE IF NOT EXISTS "Date" (
    "Id" SERIAL PRIMARY KEY,
    "DateValue" DATE UNIQUE NOT NULL,
    "Dayofweek" INT NOT NULL,
    "Weekday" TEXT NOT NULL,
    "Quarter" INT NOT NULL,
    "Year" INT NOT NULL,
    "Month" INT NOT NULL,
    "MonthName" TEXT NOT NULL,
    "Day" INT NOT NULL,
    "IsHoliday" BOOLEAN DEFAULT FALSE
);

CREATE TABLE "Brand" (
    "Id" SERIAL PRIMARY KEY, 
    "BrandName" VARCHAR(255), 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "ItemType" (
    "Id" SERIAL PRIMARY KEY, 
    "ItemTypeName" VARCHAR(255), 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Organization" (
    "Id" SERIAL PRIMARY KEY, 
    "TaxId" VARCHAR(255), 
    "OrganizationName" VARCHAR(255), 
    "Address" VARCHAR(255), 
    "MobileNumber" VARCHAR(20), 
    "Password" VARCHAR(255), 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Member" (
    "Id" SERIAL PRIMARY KEY, 
    "OrganizationId" INTEGER REFERENCES "Organization"("Id") ON DELETE SET NULL, 
    "MemberName" VARCHAR(255), 
    "BirthDate" DATE, 
    "Address" VARCHAR(255), 
    "MobileNumber" VARCHAR(20), 
    "Points" FLOAT DEFAULT 0, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Promo" (
    "Id" SERIAL PRIMARY KEY, 
    "PromoName" VARCHAR(255), 
    "DiscountRate" FLOAT, 
    "Description" VARCHAR(255), 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Reward" (
    "Id" SERIAL PRIMARY KEY, 
    "RewardName" VARCHAR(255), 
    "Points" FLOAT, 
    "Target" FLOAT, 
    "Description" VARCHAR(255), 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "SalesGroup" (
    "Id" SERIAL PRIMARY KEY, 
    "SalesGroupName" VARCHAR(255), 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE "Supplier" (
    "Id" SERIAL PRIMARY KEY, 
    "SupplierName" VARCHAR(255), 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Item" (
    "Id" SERIAL PRIMARY KEY, 
    "ItemName" VARCHAR(255), 
    "Barcode" VARCHAR(255), 
    "ExpireDate" DATE, 
    "ItemTypeId" INTEGER REFERENCES "ItemType"("Id") ON DELETE SET NULL, 
    "BrandId" INTEGER REFERENCES "Brand"("Id") ON DELETE SET NULL, 
    "SalesGroupId" INTEGER REFERENCES "SalesGroup"("Id") ON DELETE SET NULL, 
    "SupplierId" INTEGER REFERENCES "Supplier"("Id") ON DELETE SET NULL, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "ItemPrice" (
    "Id" SERIAL PRIMARY KEY, 
    "ItemId" INTEGER REFERENCES "Item"("Id") ON DELETE SET NULL, 
    "Cost" FLOAT, 
    "Price" FLOAT, 
    "PromoId" INTEGER REFERENCES "Promo"("Id") ON DELETE SET NULL, 
    "Discount" FLOAT,
    "EffectiveDate" DATE,  
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Stock" (
    "Id" SERIAL PRIMARY KEY, 
    "ItemId" INTEGER REFERENCES "Item"("Id") ON DELETE SET NULL, 
    "OnHand" INTEGER DEFAULT 0, 
    "Available" INTEGER DEFAULT 0, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "User" (
    "Id" SERIAL PRIMARY KEY, 
    "OrganizationId" INTEGER REFERENCES "Organization"("Id") ON DELETE SET NULL, 
    "UserName" VARCHAR(255), 
    "Password" VARCHAR(255), 
    "FullName" VARCHAR(255), 
    "BirthDate" DATE, 
    "MobileNumber" VARCHAR(20), 
    "AccessLevel" INTEGER, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "UserSession" (
    "Id" SERIAL PRIMARY KEY, 
    "UserId" INTEGER REFERENCES "User"("Id") ON DELETE SET NULL, 
    "ActiveStatus" INTEGER, 
    "LastLoginTs" TIMESTAMP, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "OrderType" (
    "Id" SERIAL PRIMARY KEY, 
    "OrderTypeName" TEXT, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Receipt" (
    "Id" SERIAL PRIMARY KEY,  
    "OrganizationId" INTEGER REFERENCES "Organization"("Id") ON DELETE SET NULL, 
    "UserId" INTEGER REFERENCES "User"("Id") ON DELETE SET NULL, 
    "MemberId" INTEGER REFERENCES "Member"("Id") ON DELETE SET NULL, 
    "DateId" INTEGER REFERENCES "Date"("Id") ON DELETE SET NULL, 
    "OrderTypeId" INTEGER REFERENCES "OrderType"("Id") ON DELETE SET NULL, 
    "ReferenceId" TEXT,
    "MachineId" TEXT,
    "OrderName" TEXT,
    "Billing" JSONB,
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "ItemSold" (
    "Id" SERIAL PRIMARY KEY, 
    "ReceiptId" INTEGER REFERENCES "Receipt"("Id") ON DELETE SET NULL, 
    "ItemPriceId" INTEGER REFERENCES "Item"("Id") ON DELETE SET NULL, 
    "Quantity" INTEGER, 
    "Total" FLOAT, 
    "VoidReason" VARCHAR(255), 
    "VoidStatus" INTEGER, 
    "StockBypass" INTEGER, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "POSConfig" (
    "Id" SERIAL PRIMARY KEY, 
    "OrganizationId" INTEGER REFERENCES "Organization"("Id") ON DELETE SET NULL, 
    "Config" JSONB,
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);