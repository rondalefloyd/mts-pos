import os
from dotenv import load_dotenv
from playhouse.postgres_ext import *

# Load the global .env file
load_dotenv()

# Determine which environment to load
mode = os.getenv('MODE', 'development')  # Default to 'development' if MODE is not set
load_dotenv(f'.env.{mode}')

# Retrieve environment variables
database_name = 'postgres'
database_user = 'postgres'
database_password = 'admin'
database_host = 'localhost'
database_port = '5432'
database_sslmode = 'disable'

# Initialize the database connection
postgres_db = PostgresqlExtDatabase(
    database=database_name,
    user=database_user,
    password=database_password,
    host=database_host,
    port=database_port,
    sslmode=database_sslmode,
)
