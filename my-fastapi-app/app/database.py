 # Database connection setup
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Format -> sqlite://<nohostname>/<path>
DATABASE_URL = "sqlite:///./bookshop.db"

# Create a Database Engine
# Create a connection that allows access from different threads
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Define a Dependency for Database Access
async def get_db():
    db = SessionLocal() # Create a new database session.
    try:
        yield db # Allow database access within a request, and return the session to the API endpoint.
    finally:
        db.close() # Close the session after use (prevents memory leaks)