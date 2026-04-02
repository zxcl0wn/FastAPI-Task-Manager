from fastapi import APIRouter, HTTPException
from ..database import fake_db
from ..models import CategoryResponse, CategoryCreate, CategoryUpdate
from typing import List
from ..repositories.categories_repository import CategoryRepository


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.get("/", response_model=List[CategoryResponse])
async def get_categories():
    categories = CategoryRepository(fake_db).get_all()
    return categories

@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(category_id: int):
    category = CategoryRepository(fake_db).get_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
    return category


@router.post("/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate):
    new_category = CategoryRepository(fake_db).create(category.model_dump())
    return new_category

@router.put("/{category_id}", response_model=CategoryResponse)
async def put_category(category_id: int, new_category_data: CategoryUpdate):
    updated_category = CategoryRepository(fake_db).update(category_id, new_category_data.model_dump())
    if not updated_category:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
    return updated_category

@router.delete("/{category_id}", response_model=CategoryResponse)
async def delete_category(category_id: int):
    deleted_category = CategoryRepository(fake_db).delete(category_id)
    if not deleted_category:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
    return deleted_category