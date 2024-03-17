from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm import sessionmaker
import os 
SQLALCHEMY_DATABASE_URL = "postgres://default:8t5QxvHanDpC@ep-aged-pond-a2motml2-pooler.eu-central-1.aws.neon.tech/verceldb?sslmode=require" 
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() 
