from fastapi.testclient import TestClient
from app import main
import pytest

client = TestClient(main.app)


# TODO: Need a test fixture to create some data

# Test home func
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my bookshop!"}


def test_add_book():
    response = client.post(
        "/add-books/",
        json={"title": "1984", "author": "George Orwell", "price": 9.99, "stock": 10}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "1984"

def test_list_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_book():
    book_id = 1  # Assuming the first book added
    response = client.delete(f"/books/{book_id}")
    assert response.status_code in [200, 404]  # Can be already deleted