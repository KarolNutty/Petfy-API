from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./pets.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)  # autocommit tem que ser False mesmo
Base = declarative_base()

def create_db():
    from app.models.pet import Pet  # importa o model pra registrar
    Base.metadata.create_all(bind=engine)


