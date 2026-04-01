from fastapi import APIRouter, HTTPException
from ..database import fake_db
from ..models import CategoryResponse, CategoryCreate, CategoryUpdate
from typing import List


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.get("/", response_model=List[CategoryResponse])
async def get_categories():
    return list(fake_db["categories"].values())

@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(category_id: int):
    try:
        return fake_db["categories"][category_id]
    except:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")

@router.post("/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate):
    id = len(fake_db["categories"])+1
    new_category = {"id": id, **category.model_dump()}
    fake_db["categories"][id] = new_category
    return new_category

@router.put("/{category_id}", response_model=CategoryResponse)
async def put_category(category_id: int, new_category_data: CategoryUpdate):
    try:
        new_category = fake_db["categories"][category_id]
        new_category.update(new_category_data.model_dump())
        return new_category
    except:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")

@router.delete("/{category_id}", response_model=CategoryResponse)
async def delete_category(category_id: int):
    try:
        category = fake_db["categories"][category_id]
        del fake_db["categories"][category_id]
        return category
    except:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
