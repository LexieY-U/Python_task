## Introduction
📚 FastAPI Bookshop API
A simple FastAPI-based bookshop RESTful API with SQLite database, featuring:

## Features
- **CRUD operations**: (Create, Read, Delete books)
- **Database Integration**: Persistent storage using **SQLite** with SQLAlchemy ORM.
- **Pydantic validation**: Request data
- **SQLAlchemy ORM**: database management
- Logging & Observability
- Automated tests with Pytest

## 🚀 Getting Started
1️⃣ Clone the Repository
 ```bash
git clone https://github.com/your-username/my-fastapi-app.git
cd my-fastapi-app
```
2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Run the FastAPI Server
```bash
uvicorn main:app --host 0.0.0.0 --port 9000 --reload
```
Server will run at:
```bash
http://127.0.0.1:9000
```

## 🛠 API Endpoints
### 📌 Home
GET / → Returns welcome message.

### 📌 Books
GET /books/ → List all books
POST /add-books/ → Add a new book

### Request Body (JSON):
```json
json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "price": 12.99,
  "stock": 5
}
{
  "title": "1984",
  "author": "George Orwell",
  "price": 14.99,
  "stock": 10
}

{
  "title": "To Kill a Mockingbird",
  "author": "Harper Lee",
  "price": 12.49,
  "stock": 7
}
```

### DELETE 
/books/{book_id} → Remove a book

### 🧪 Running Tests
To run unit tests:
```bash
pytest
```

## 🛠 Project Structure

```
my-fastapi-app/
│── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app entry point
│   ├── database.py      # Database connection setup
│   ├── models.py        # SQLAlchemy ORM models
│   ├── schemas.py       # Pydantic models for validation
│   ├── crud.py          # CRUD operations for database
│   ├── logging_config.py# Logging setup for observability
│── tests/
|   ├── __init__.py
│   ├── test_main.py    # Pytest test cases
│── requirements.txt
│── .gitignore
│── README.md
```
          
📜 License
This project is open-source and available under the MIT License.
