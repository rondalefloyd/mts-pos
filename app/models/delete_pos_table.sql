-- Disable foreign key checks temporarily if your database supports it
-- (for example, in MySQL you can use SET FOREIGN_KEY_CHECKS=0; and later SET FOREIGN_KEY_CHECKS=1;)

-- Delete from tables that do not have foreign key dependencies first
DELETE FROM "UserSessionInfos";
DELETE FROM "ItemPrices";
DELETE FROM "Stocks";
DELETE FROM "Members";

-- Delete from tables that have foreign key dependencies next
DELETE FROM "Items";
DELETE FROM "Users";

-- Finally, delete from the remaining tables
DELETE FROM "Brands";
DELETE FROM "ItemTypes";
DELETE FROM "Organizations";
DELETE FROM "Promos";
DELETE FROM "SalesGroups";
DELETE FROM "Suppliers";


-- Drop the Dates table if it exists
DROP TABLE IF EXISTS "Dates";

-- Optionally, re-enable foreign key checks if you disabled them earlier
-- (for example, in MySQL you can use SET FOREIGN_KEY_CHECKS=1;)
