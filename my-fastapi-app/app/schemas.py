# Pydantic models for validation

from pydantic import BaseModel, Field

# Create book schema
class BookCreate(BaseModel):
    id: int
    title: str = Field(..., min_length=1, max_length=100) # Field Validation
    author: str = Field(..., min_length=1, max_length=50)
    price: float = Field(..., gt=0)  # Price must be > 0; gt -> greater than
    stock: int = Field(..., ge=0)    # Stock must be >= 0 -> greater and equal than

# Create response format when retrieving books from the database
# Inherits all fields from BookCreate, plus an ID
class BookResponse(BookCreate):
    id: int

    # Customise model behavior using the Config class
    class Config:
        # Enable automatic conversion from database models to Pydantic models.
        orm_mode = True
