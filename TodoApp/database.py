from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

PRODUCTION_DB = 'postgresql://postgres:test123@localhost/TodoApplicationDatabase'
TEST_DB = 'sqlite:///./todosapp.db'

engine = create_engine(TEST_DB, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
