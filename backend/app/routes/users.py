from fastapi import APIRouter, HTTPException
from ..database import fake_db
from ..models import UserCreate, UserUpdate, UserResponse
from typing import List
from ..repositories.users_repository import UserRepository


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=List[UserResponse])
async def get_users():
    users = UserRepository(fake_db).get_all()
    return users

@router.get('/{user_id}', response_model=UserResponse)
async def get_user(user_id: int):
    user = UserRepository(fake_db).get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user


@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    new_user = UserRepository(fake_db).create(user.model_dump())
    return new_user

@router.put("/{user_id}", response_model=UserResponse)
async def put_user(user_id: int, new_user_data: UserUpdate):
    updated_user = UserRepository(fake_db).update(user_id, new_user_data.model_dump())
    if not updated_user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return updated_user

@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int):
    deleted_user = UserRepository(fake_db).delete(user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return deleted_user