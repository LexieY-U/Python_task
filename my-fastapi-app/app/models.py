# SQLAlchemy ORM models creation

from sqlalchemy import Column, Integer, String, Float
from database import Base

# Create a base class for ORM models - every model will inherit from this class.
class Book(Base):
    # Set the table name to "books" - SQLAlchemy will create a table with this name in the database.
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True, nullable=False) # Cannot be empty (required field)
    author = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
