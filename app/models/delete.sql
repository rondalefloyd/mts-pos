-- Delete from dependent tables first to ensure referential integrity
DELETE FROM "ItemPrice";
DELETE FROM "Stock";
DELETE FROM "UserSession";
DELETE FROM "ItemSold";
DELETE FROM "Receipt";
DELETE FROM "POSConfig";

-- Delete from main tables
DELETE FROM "User";
DELETE FROM "Member";
DELETE FROM "Item";
DELETE FROM "Organization";
DELETE FROM "Brand";
DELETE FROM "ItemType";
DELETE FROM "Promo";
DELETE FROM "Reward";
DELETE FROM "SalesGroup";
DELETE FROM "Supplier";
DELETE FROM "OrderType";

-- The cascading delete will automatically take care of the dependent records in the child tables.