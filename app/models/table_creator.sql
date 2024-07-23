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