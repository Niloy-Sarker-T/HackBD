from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:N1loys%40rker@localhost:5432/hackathon_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
