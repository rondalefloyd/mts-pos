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