CREATE TABLE "Brands" (
    "Id" SERIAL PRIMARY KEY, 
    "BrandName" VARCHAR(255) UNIQUE, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "ItemTypes" (
    "Id" SERIAL PRIMARY KEY, 
    "ItemTypeName" VARCHAR(255) UNIQUE, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Organizations" (
    "Id" SERIAL PRIMARY KEY, 
    "TaxId" VARCHAR(255) UNIQUE, 
    "OrganizationName" VARCHAR(255) UNIQUE, 
    "Address" VARCHAR(255), 
    "MobileNumber" VARCHAR(20), 
    "AccessCode" VARCHAR(255), 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Members" (
    "Id" SERIAL PRIMARY KEY, 
    "OrganizationId" INTEGER REFERENCES "Organizations"("Id") ON DELETE CASCADE, 
    "MemberName" VARCHAR(255) UNIQUE, 
    "BirthDate" DATE, 
    "Address" VARCHAR(255), 
    "MobileNumber" VARCHAR(20), 
    "Points" FLOAT, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Promos" (
    "Id" SERIAL PRIMARY KEY, 
    "PromoName" VARCHAR(255) UNIQUE, 
    "DiscountRate" FLOAT, 
    "Description" VARCHAR(255), 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Rewards" (
    "Id" SERIAL PRIMARY KEY, 
    "RewardName" VARCHAR(255) UNIQUE, 
    "Points" FLOAT, 
    "Target" FLOAT, 
    "Description" VARCHAR(255), 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "SalesGroups" (
    "Id" SERIAL PRIMARY KEY, 
    "SalesGroupName" VARCHAR(255) UNIQUE, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO "SalesGroups" ("Id", "SalesGroupName") VALUES 
(1, 'RETAIL'), 
(2, 'WHOLESALE');

CREATE TABLE "Suppliers" (
    "Id" SERIAL PRIMARY KEY, 
    "SupplierName" VARCHAR(255) UNIQUE, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Items" (
    "Id" SERIAL PRIMARY KEY, 
    "ItemName" VARCHAR(255), 
    "Barcode" VARCHAR(255), 
    "ExpireDate" DATE, 
    "ItemTypeId" INTEGER REFERENCES "ItemTypes"("Id") ON DELETE CASCADE, 
    "BrandId" INTEGER REFERENCES "Brands"("Id") ON DELETE CASCADE, 
    "SalesGroupId" INTEGER REFERENCES "SalesGroups"("Id") ON DELETE CASCADE, 
    "SupplierId" INTEGER REFERENCES "Suppliers"("Id") ON DELETE CASCADE, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_itemname_salesgroup UNIQUE ("ItemName", "SalesGroupId")
);

CREATE TABLE "Stocks" (
    "Id" SERIAL PRIMARY KEY, 
    "ItemId" INTEGER REFERENCES "Items"("Id") ON DELETE CASCADE, 
    "OnHand" INTEGER, 
    "Available" INTEGER, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "ItemPrices" (
    "Id" SERIAL PRIMARY KEY, 
    "ItemId" INTEGER REFERENCES "Items"("Id") ON DELETE CASCADE, 
    "Capital" FLOAT, 
    "Price" FLOAT, 
    "PromoId" INTEGER REFERENCES "Promos"("Id") ON DELETE CASCADE, 
    "Discount" FLOAT,
    "EffectiveDate" DATE,  
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_itemprice_combination UNIQUE ("ItemId", "Capital", "Price", "PromoId", "Discount", "EffectiveDate")
);

CREATE TABLE "Users" (
    "Id" SERIAL PRIMARY KEY, 
    "OrganizationId" INTEGER REFERENCES "Organizations"("Id") ON DELETE CASCADE, 
    "UserName" VARCHAR(255) UNIQUE, 
    "AccessCode" VARCHAR(255), 
    "FullName" VARCHAR(255), 
    "BirthDate" DATE, 
    "MobileNumber" VARCHAR(20), 
    "AccessLevel" INTEGER, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "UserSessionInfos" (
    "Id" SERIAL PRIMARY KEY, 
    "UserId" INTEGER REFERENCES "Users"("Id") ON DELETE CASCADE, 
    "ActiveStatus" INTEGER, 
    "LastLoginTs" TIMESTAMP, 
    "LastLogoutTs" TIMESTAMP, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- Create the Dates table
CREATE TABLE IF NOT EXISTS "Dates" (
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
INSERT INTO "Dates" ("DateValue", "Dayofweek", "Weekday", "Quarter", "Year", "Month", "MonthName", "Day")
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
UPDATE "Dates"
SET "IsHoliday" = TRUE
WHERE   
    ("Month" = 1 AND "Day" = 1) OR
    ("Month" = 11 AND "Day" BETWEEN 29 AND 30) OR
    ("Month" = 12 AND "Day" BETWEEN 24 AND 31);

-- for transaction db
CREATE TABLE "Sales" (
    "Id" SERIAL PRIMARY KEY, 
    "UserId" INTEGER REFERENCES "Users"("Id") ON DELETE CASCADE, 
    "CustomerId" INTEGER REFERENCES "Members"("Id") ON DELETE CASCADE, 
    "ItemId" INTEGER REFERENCES "Items"("Id") ON DELETE CASCADE, 
    "Quantity" INTEGER, 
    "QuantityPrice" FLOAT, 
    "Reason" TEXT, 
    "ReferenceId" TEXT, 
    "Status" INTEGER, 
    "DateId" INTEGER REFERENCES "Dates"("Id") ON DELETE CASCADE, 
    "UpdateTs" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);