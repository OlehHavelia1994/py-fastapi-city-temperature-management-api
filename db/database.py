from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = "sqlite:///city.db"
engine = create_engine(DATABASE_URL, connect_args={"autocommit": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit= False)

class Base(DeclarativeBase):
    pass
