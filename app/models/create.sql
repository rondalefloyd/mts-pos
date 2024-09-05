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
    "AccessCode" VARCHAR(255), 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Member" (
    "Id" SERIAL PRIMARY KEY, 
    "OrganizationId" INTEGER REFERENCES "Organization"("Id") ON DELETE CASCADE, 
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
    "ItemTypeId" INTEGER REFERENCES "ItemType"("Id") ON DELETE CASCADE, 
    "BrandId" INTEGER REFERENCES "Brand"("Id") ON DELETE CASCADE, 
    "SalesGroupId" INTEGER REFERENCES "SalesGroup"("Id") ON DELETE CASCADE, 
    "SupplierId" INTEGER REFERENCES "Supplier"("Id") ON DELETE CASCADE, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "ItemPrice" (
    "Id" SERIAL PRIMARY KEY, 
    "ItemId" INTEGER REFERENCES "Item"("Id") ON DELETE CASCADE, 
    "Capital" FLOAT, 
    "Price" FLOAT, 
    "PromoId" INTEGER REFERENCES "Promo"("Id") ON DELETE CASCADE, 
    "Discount" FLOAT,
    "EffectiveDate" DATE,  
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Stock" (
    "Id" SERIAL PRIMARY KEY, 
    "ItemId" INTEGER REFERENCES "Item"("Id") ON DELETE CASCADE, 
    "OnHand" INTEGER DEFAULT 0, 
    "Available" INTEGER DEFAULT 0, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "User" (
    "Id" SERIAL PRIMARY KEY, 
    "OrganizationId" INTEGER REFERENCES "Organization"("Id") ON DELETE CASCADE, 
    "UserName" VARCHAR(255), 
    "AccessCode" VARCHAR(255), 
    "FullName" VARCHAR(255), 
    "BirthDate" DATE, 
    "MobileNumber" VARCHAR(20), 
    "AccessLevel" INTEGER, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "UserSession" (
    "Id" SERIAL PRIMARY KEY, 
    "UserId" INTEGER REFERENCES "User"("Id") ON DELETE CASCADE, 
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
    "OrganizationId" INTEGER REFERENCES "Organization"("Id") ON DELETE CASCADE, 
    "UserId" INTEGER REFERENCES "User"("Id") ON DELETE CASCADE, 
    "MemberId" INTEGER REFERENCES "Member"("Id") ON DELETE CASCADE, 
    "DateId" INTEGER REFERENCES "Date"("Id") ON DELETE CASCADE, 
    "OrderTypeId" INTEGER REFERENCES "OrderType"("Id") ON DELETE CASCADE, 
    "ReferenceId" TEXT,
    "OrderName" TEXT,
    "OrderSummary" JSONB,
    "OrderPayment" JSONB,
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "ItemSold" (
    "Id" SERIAL PRIMARY KEY, 
    "ReceiptId" INTEGER REFERENCES "Receipt"("Id") ON DELETE CASCADE, 
    "ItemId" INTEGER REFERENCES "Item"("Id") ON DELETE CASCADE, 
    "Quantity" INTEGER, 
    "Total" FLOAT, 
    "VoidReason" VARCHAR(255), 
    "VoidStatus" INTEGER, 
    "StockBypass" INTEGER, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE "POSConfig" (
    "Id" SERIAL PRIMARY KEY, 
    "OrganizationId" INTEGER REFERENCES "Organization"("Id") ON DELETE CASCADE, 
    "Config" JSONB,
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);