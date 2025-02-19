# CRUD operations for database

from sqlalchemy.orm import Session
from schemas import BookCreate
from models import Book
from logging_config import logger


# Book CRUD operations
def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)  # Add book to database session
    db.commit() # Save changes to database
    db.refresh(db_book)  # Reload book from database with assigned ID
    logger.info(f"Book added: {db_book.title} by {db_book.author}") # Log the action for observability
    return db_book  # Return the created book

def get_books(db: Session):
    return db.query(Book).all()  # Fetch all books from the database


def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        logger.info(f"Book deleted: {book.title}")
        return book
    return None