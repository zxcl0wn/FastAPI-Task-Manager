from pydantic import BaseModel, Field


class BaseCategory(BaseModel):
    title: str = Field(..., min_length=3, max_length=20, description="Category title")


class CategoryCreate(BaseCategory):
    ...


class CategoryResponse(BaseCategory):
    id: int = Field(..., description="Category ID")

    class Config:
        from_attributes = True


class CategoryUpdate(BaseCategory):
    title: str|None = None
