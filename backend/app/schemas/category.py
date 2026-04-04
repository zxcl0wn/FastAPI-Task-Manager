from pydantic import BaseModel, Field


class BaseCategory(BaseModel):
    title: str = Field(..., min_length=5, max_length=20, description="Category title")

class CategoryCreate(BaseCategory):
    ...

class CategoryResponse(BaseCategory):
    id: int = Field(..., description="Category ID")

class CategoryUpdate(BaseCategory):
    title: str|None = None
