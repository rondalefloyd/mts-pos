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