import os, sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(''))
from app.models.model_association import Organization

tursoUrl = f"{os.getenv('ONLINE_SQLALCHEMY_BASE_URL')}://{os.getenv('TURSO_DB_URL')}/?authToken={os.getenv('TURSO_DB_AUTH_TOKEN')}"
localUrl = f"{os.getenv('OFFLINE_SQLALCHEMY_BASE_URL')}:///{os.getenv('OFFLINE_DB_FILE_PATH')}/pos.db"

try:
    engine = create_engine(url=tursoUrl, echo=False)
    session = sessionmaker(bind=engine)()
    status = 'ONLINE'
    
except Exception as error:
    print('Something went wrong:', error)