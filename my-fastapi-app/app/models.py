from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# Create a base class for ORM models - every model will inherit from this class.
class Book(Base):
    # Set the table name to "books" - SQLAlchemy will create a table with this name in the database.
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False) # Cannot be empty (required field)
    author = Column(String, index=True, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
