import os, sys
from peewee import *

sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.entities import User
from app.utils.databases import postgres_db

# Connect to the database
postgres_db.connect()

# Query the User table
users = User.select()

# Print the users
print("Users in the database:")
for user in users:
    print(user.Id, user.UserName, user.FullName)

# Close the database connection
postgres_db.close()
