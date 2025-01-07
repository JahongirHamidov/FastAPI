from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

PRODUCTION_DB = 'postgresql://database_rhhk_user:s8u3osWf7fUYpSDywRZ6Zc28IamuQ5iz@dpg-ctui9gi3esus739cml1g-a.oregon-postgres.render.com/database_rhhk'
# TEST_DB = 'sqlite:///./todosapp.db'

engine = create_engine(PRODUCTION_DB)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()