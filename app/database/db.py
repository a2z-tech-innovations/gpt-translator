import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./sql_app.db')
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
