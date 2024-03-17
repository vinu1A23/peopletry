from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm import sessionmaker
import os 
if os.getcwd()[-1:]=='i':
    SQLALCHEMY_DATABASE_URL= os.environ["LOCAL_POSTGRES_URL"]
    print(SQLALCHEMY_DATABASE_URL)
else:
    SQLALCHEMY_DATABASE_URL = os.environ["POSTGRES_URL"]
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() 
