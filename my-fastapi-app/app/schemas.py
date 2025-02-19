from pydantic import BaseModel, Field

# Create book schema
class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100) # Field Validation
    author: str = Field(..., min_length=1, max_length=50)
    price: float = Field(..., gt=0)  # Price must be > 0; gt -> greater than
    stock: int = Field(..., ge=0)    # Stock must be >= 0 -> greater and equal than

class BookResponse(BookCreate):
    id: int

    # Customise model behavior using the Config class
    class Config:
        # This allows the model to work with ORMs by reading data from attributes instead of dict keys
        orm_mode = True
