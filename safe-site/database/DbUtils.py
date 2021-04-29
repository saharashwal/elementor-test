from sqlalchemy.ext.declarative import declarative_base
from database.config import database as db_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

class DbUtils:

    def __init__(self):
        self.db = create_engine(f"mssql+pymssql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['db_name']}")
        Base.metadata.create_all(self.db)

        # create a configured "Session" class
        Session = sessionmaker(bind=self.db)

        # create a Session
        self.session = Session()