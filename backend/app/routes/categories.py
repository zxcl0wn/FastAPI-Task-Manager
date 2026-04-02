from fastapi import APIRouter, HTTPException
from ..database import fake_db
from ..models import CategoryResponse, CategoryCreate, CategoryUpdate
from typing import List
from ..services import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.get("/", response_model=List[CategoryResponse])
async def get_categories():
    service = CategoryService(fake_db)
    return service.get_all()

@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(category_id: int):
    service = CategoryService(fake_db)
    return service.get_by_id(category_id)

@router.post("/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate):
    service = CategoryService(fake_db)
    return service.create(category.model_dump())

@router.put("/{category_id}", response_model=CategoryResponse)
async def put_category(category_id: int, new_category_data: CategoryUpdate):
    service = CategoryService(fake_db)
    return service.update(category_id, new_category_data.model_dump())

@router.delete("/{category_id}", response_model=CategoryResponse)
async def delete_category(category_id: int):
    service = CategoryService(fake_db)
    return service.delete(category_id)