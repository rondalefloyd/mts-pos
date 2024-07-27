from dotenv import load_dotenv
import os
from playhouse.postgres_ext import PostgresqlExtDatabase

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
database_name = os.getenv('DATABASE_NAME')
database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
database_host = os.getenv('DATABASE_HOST')
database_port = int(os.getenv('DATABASE_PORT'))
database_sslmode = os.getenv('DATABASE_SSLMODE')

postgres_db = PostgresqlExtDatabase(
    database=database_name,
    user=database_user,
    password=database_password,
    host=database_host,
    port=database_port,
    sslmode=database_sslmode,
)