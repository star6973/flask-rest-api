from sqlalchemy import create_engine, Column, Integer, Float, String, JSON
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DBSession = scoped_session(sessionmaker())

def init_database(name="sqlite:///database/flask_database.db"):
    print("데이터베이스 초기화!!")
    engine = create_engine(name, echo=False)
    DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)

    return DBSession