from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///database.db"
# DATABASE_URL = "postgresql://postgres:ZOPH1qjPAmZ4azDM@db.sebxtxqbobosundybxwy.supabase.co:5432/postgres"
# DATABASE_URL = "postgres-production-3f84.up.railway.app"

Base = declarative_base()
# engine = create_engine(DATABSER_URL, connect_args={"check_same_thread" : False})
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close_all()
