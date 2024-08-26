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

INSERT INTO "SalesGroup" ("Id", "SalesGroupName") VALUES 
(1, 'RETAIL'), 
(2, 'WHOLESALE');

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

-- Insert dates from 1980-01-01 to 3000-01-01
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

-- Update the IsHoliday field for specific dates
UPDATE "Date"
SET "IsHoliday" = TRUE
WHERE   
    ("Month" = 1 AND "Day" = 1) OR
    ("Month" = 11 AND "Day" BETWEEN 29 AND 30) OR
    ("Month" = 12 AND "Day" BETWEEN 24 AND 31);

-- for transaction db

CREATE TABLE "OrderType" (
    "Id" SERIAL PRIMARY KEY, 
    "OrderTypeName" TEXT, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO "OrderType" ("Id", "OrderTypeName") VALUES 
(1, 'RETAIL'), 
(2, 'WHOLESALE'), 
(3, 'MIXED');

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

CREATE TABLE "Reason" (
    "Id" SERIAL PRIMARY KEY, 
    "ReasonName" TEXT, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO "Reason" ("ReasonName") VALUES
('Customer Request'),
('Damaged Item'),
('Inventory Adjustment'),
('Promotion Discount'),
('Price Correction');

CREATE TABLE "ItemSold" (
    "Id" SERIAL PRIMARY KEY, 
    "ReceiptId" INTEGER REFERENCES "Receipt"("Id") ON DELETE CASCADE, 
    "ItemId" INTEGER REFERENCES "Item"("Id") ON DELETE CASCADE, 
    "Quantity" INTEGER, 
    "Total" FLOAT, 
    "ReasonId" INTEGER REFERENCES "Reason"("Id") ON DELETE CASCADE, 
    "Status" INTEGER, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE "POSConfig" (
    "Id" SERIAL PRIMARY KEY, 
    "OrganizationId" INTEGER REFERENCES "Organization"("Id") ON DELETE CASCADE, 
    "Config" JSONB,
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
