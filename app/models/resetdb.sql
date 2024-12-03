-- DROP ALL EXISTING TABLE
-- Drop dependent tables first to avoid foreign key constraint issues
DROP TABLE IF EXISTS "ItemPrice" CASCADE;
DROP TABLE IF EXISTS "Stock" CASCADE;
DROP TABLE IF EXISTS "UserSession" CASCADE;
DROP TABLE IF EXISTS "ItemSold" CASCADE;
DROP TABLE IF EXISTS "Receipt" CASCADE;
DROP TABLE IF EXISTS "POSConfig" CASCADE;

-- Drop main tables
DROP TABLE IF EXISTS "User" CASCADE;
DROP TABLE IF EXISTS "Member" CASCADE;
DROP TABLE IF EXISTS "Item" CASCADE;
DROP TABLE IF EXISTS "Organization" CASCADE;
DROP TABLE IF EXISTS "Brand" CASCADE;
DROP TABLE IF EXISTS "ItemType" CASCADE;
DROP TABLE IF EXISTS "Promo" CASCADE;
DROP TABLE IF EXISTS "Reward" CASCADE;
DROP TABLE IF EXISTS "SalesGroup" CASCADE;
DROP TABLE IF EXISTS "Supplier" CASCADE;
DROP TABLE IF EXISTS "OrderType" CASCADE;
DROP TABLE IF EXISTS "Date" CASCADE;

-- CREATE NEW TABLE
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
    "DateId" INTEGER REFERENCES "Date"("Id") ON DELETE SET NULL, 
    "UserId" INTEGER REFERENCES "User"("Id") ON DELETE SET NULL, 
    "MemberId" INTEGER REFERENCES "Member"("Id") ON DELETE SET NULL, 
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



-- INSERT INITIAL DATA

INSERT INTO "Date" ("DateValue", "Dayofweek", "Weekday", "Quarter", "Year", "Month", "MonthName", "Day")
SELECT 
    date::DATE AS "DateValue",
    EXTRACT(DOW FROM date) AS "Dayofweek",
    TO_CHAR(date, 'Day') AS "Weekday",
    EXTRACT(QUARTER FROM date) AS "Quarter",
    EXTRACT(YEAR FROM date) AS "Year",
    EXTRACT(MONTH FROM date) AS "Month",
    TO_CHAR(date, 'Mon') AS "MonthName",
    EXTRACT(DAY FROM date) AS "Day"
FROM 
    generate_series('1980-01-01'::DATE, '3000-01-01'::DATE, '1 day'::INTERVAL) date;

INSERT INTO "Organization" ("TaxId", "OrganizationName", "Address", "MobileNumber", "Password") VALUES 
('123456', 'MTS INC.', 'ANABU 1C, IMUS, CAVITE', '09123456789', 'admin');

-- MAKE SURE TO CHANGE THE ORGANIZATION NAME VALUE
INSERT INTO "POSConfig" ("OrganizationId", "Config") VALUES 
(
    (SELECT "Id" FROM "Organization" WHERE "OrganizationName" = 'MTS INC.'),
    '{
        "color_scheme": "PROTO",
        "page_limit": 30,
        "cloud_storage": 1,
        "currency_symbol": "₱"
    }'
);

-- MAKE SURE TO CHANGE THE ORGANIZATION NAME VALUE
INSERT INTO "User" ("OrganizationId", "UserName", "Password", "FullName", "BirthDate", "MobileNumber", "AccessLevel") VALUES 
((SELECT "Id" FROM "Organization" WHERE "OrganizationName" = 'MTS INC.'), 'admin', 'admin', 'JUAN DELA CRUZ', '2000-01-01', '09123456789', 3);

INSERT INTO "UserSession" ("UserId", "ActiveStatus") VALUES 
((SELECT "Id" FROM "User" WHERE "UserName" = 'admin'), 0);


-- MAKE SURE TO CHANGE THE ORGANIZATION NAME VALUE
INSERT INTO "Member" ("OrganizationId", "MemberName", "BirthDate", "Address", "MobileNumber", "Points") VALUES 
((SELECT "Id" FROM "Organization" WHERE "OrganizationName" = 'MTS INC.'), 'JUAN', '2000-01-01', 'ANABU 1C, IMUS, CAVITE', '09123456789', '100');

INSERT INTO "SalesGroup" ("Id", "SalesGroupName") VALUES 
(1, 'RETAIL'), 
(2, 'WHOLESALE');

INSERT INTO "OrderType" ("Id", "OrderTypeName") VALUES 
(1, 'RETAIL'), 
(2, 'WHOLESALE'), 
(3, 'MIXED');



-- UPDATE DATES TABLE
UPDATE "Date"
SET "IsHoliday" = TRUE
WHERE   
    ("Month" = 1 AND "Day" = 1) OR
    ("Month" = 11 AND "Day" BETWEEN 29 AND 30) OR
    ("Month" = 12 AND "Day" BETWEEN 24 AND 31);