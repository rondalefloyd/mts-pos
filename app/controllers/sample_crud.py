import os, sys
from peewee import *

# TODO: move this to models
sys.path.append(os.path.abspath('')) # required to change the default path
from app.models.model_association import User
from app.utils.database import db

# Connect to the database
db.connect()

# Query the User table
users = User.select()

# Print the users
print("Users in the database:")
for user in users:
    print(user.Id, user.UserName, user.FullName)

# Close the database connection
db.close()
