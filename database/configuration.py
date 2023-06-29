
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
import os


# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:mailong2000@localhost:3306/factory'
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:tum19@localhost/factory"
# ROOT_DATA = 'data'
# IMAGES_DIR = os.path.join(ROOT_DATA, 'images')
# os.makedirs(IMAGES_DIR, exist_ok=True)


# host = "0.0.0.0"
# port = 8000
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
# , connect_args={"check_same_thread": False}
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    """
    Get the database session
    Yields:
        Session: The database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
