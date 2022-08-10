
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from create_connection import generate_engine, db_session
from computer import Computer


metadata = MetaData()
db_session()

def init_db():
    metadata.create_all(bind = generate_engine())