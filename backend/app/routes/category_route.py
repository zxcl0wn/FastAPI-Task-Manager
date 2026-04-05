from fastapi import APIRouter, Depends
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas.category_schema import CategoryResponse, CategoryCreate, CategoryUpdate
from typing import List
from ..services import CategoryService


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.get("/", response_model=List[CategoryResponse])
async def get_categories(db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_all()

@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(category_id: int, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_by_id(category_id)

@router.post("/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.create(category.model_dump())

@router.put("/{category_id}", response_model=CategoryResponse)
async def put_category(category_id: int, new_category_data: CategoryUpdate, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.update(category_id, new_category_data.model_dump())

@router.delete("/{category_id}", response_model=CategoryResponse)
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    service = CategoryService(db)
    return service.delete(category_id)