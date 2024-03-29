from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.data.sqlalchemy_models import Base

DB_URL = "postgresql://postgres:sql@localhost:5432/fastapi-orm"

engine = create_engine(DB_URL)

Base.metadata.create_all(engine)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
