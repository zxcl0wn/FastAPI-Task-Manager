from fastapi import APIRouter, HTTPException
from ..database import fake_db
from ..models import UserCreate, UserUpdate, UserResponse
from typing import List


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=List[UserResponse])
async def get_users():
    return list(fake_db["users"].values())

@router.get('/{user_id}', response_model=UserResponse)
async def get_user(user_id: int):
    try:
        return fake_db["users"][user_id]
    except:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    id = len(fake_db["users"])+1
    new_user = {"id": id, **user.model_dump()}
    fake_db["users"][id] = new_user
    return new_user

@router.put("/{user_id}", response_model=UserResponse)
async def put_user(user_id: int, new_user_data:UserUpdate):
    try:
        new_user = fake_db["users"][user_id]
        new_user.update(new_user_data.model_dump())
        return new_user
    except:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int):
    try:
        user = fake_db["users"][user_id]
        del fake_db["users"][user_id]
        return user
    except:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")