from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase

# Database connection details
db = PostgresqlExtDatabase(
    'mts-pos',
    user='mts-pos_owner',
    password='Eha9HrAQ1foV',
    host='ep-plain-hat-a1m6h9ar.ap-southeast-1.aws.neon.tech',
    port=5432,
    sslmode='require'
)

# Define the User model
class User(Model):
    Id = AutoField()
    OrganizationId = IntegerField(null=True)
    UserName = CharField(max_length=255, null=True)
    AccessCode = CharField(max_length=255, null=True)
    FullName = CharField(max_length=255, null=True)
    BirthDate = DateField(null=True)
    MobileNumber = CharField(max_length=20, null=True)
    AccessLevel = IntegerField(null=True)
    ActiveStatus = IntegerField(null=True)
    LastLoginTs = DateTimeField(null=True)
    LastLogoutTs = DateTimeField(null=True)
    UpdateTs = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = 'User'

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
