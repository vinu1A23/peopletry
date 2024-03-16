from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:curiouspigonabike@localhost:5432/task?connect_timeout=10&sslmode=prefer"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()