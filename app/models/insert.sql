
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

INSERT INTO "Organization" ("TaxId", "OrganizationName", "Address", "MobileNumber", "AccessCode") VALUES 
('123456', 'MTS INC.', 'ANABU 1C, IMUS, CAVITE', '09123456789', 'admin');

-- MAKE SURE TO CHANGE THE ORGANIZATION NAME VALUE
INSERT INTO "POSConfig" ("OrganizationId", "Config") VALUES 
(
    (SELECT "Id" FROM "Organization" WHERE "OrganizationName" = 'MTS INC.'),
    '{
        "color_scheme": "PROTO",
        "page_limit": 30,
        "cloud_storage": 1
    }'
);

-- MAKE SURE TO CHANGE THE ORGANIZATION NAME VALUE
INSERT INTO "User" ("OrganizationId", "UserName", "AccessCode", "FullName", "BirthDate", "MobileNumber", "AccessLevel") VALUES 
((SELECT "Id" FROM "Organization" WHERE "OrganizationName" = 'MTS INC.'), 'admin', 'admin', 'JUAN DELA CRUZ', '2000-01-01', '09123456789', 3);

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



