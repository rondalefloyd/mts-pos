import os, sys
from playhouse.postgres_ext import PostgresqlExtDatabase

sys.path.append(os.path.abspath('')) # required to change the default path

postgres_db = PostgresqlExtDatabase(
    'mts-pos',
    user='mts-pos_owner',
    password='Eha9HrAQ1foV',
    host='ep-plain-hat-a1m6h9ar.ap-southeast-1.aws.neon.tech',
    port=5432,
    sslmode='require'
)