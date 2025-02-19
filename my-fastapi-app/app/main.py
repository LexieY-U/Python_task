# FastAPI app entry point

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db, SessionLocal
from schemas import BookCreate, BookResponse
from curd import create_book, get_books, delete_book


# Create database tables
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Import the FastAPI class from the fastapi package and initialize a new FastAPI instance.
app = FastAPI()


# Define a GET endpoint that will return a simple welcome message. 
# Use the @app.get decorator to specify the route and the HTTP method.
@app.get("/") # this endpoint will respond to GET requests at the root URL path (/)
async def home(): # defines an asynchronous function named read_root that will handle incoming requests to this endpoint.
    return {"message": "Welcome to my bookshop!"} # returns a JSON response


@app.post("/add-books/", response_model=BookResponse)
async def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@app.get("/add-books/", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db)):
    return get_books(db)

@app.delete("/books/{book_id}")
def remove_book(book_id: int, db: Session = Depends(get_db)):
    book = delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}