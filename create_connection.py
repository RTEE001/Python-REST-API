import os
from dotenv import load_dotenv
from requests import session
from sqlalchemy import (
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv() 

URL = os.getenv("URL")


def generate_engine():
    engine = create_engine(
        f"{URL}",
        echo=True,
    )

    return engine

def create_session():

    engine = generate_engine()
    Base = declarative_base()
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)

    return Session

def db_session():
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=generate_engine()))
    return db_session