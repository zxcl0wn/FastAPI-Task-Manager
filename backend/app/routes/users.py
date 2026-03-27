from fastapi import APIRouter
from ..database import fake_db, id
from ..models import UserCreate, UserUpdate, UserResponse
from typing import List


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=List[UserResponse])
async def get_users():
    return fake_db["users"]

@router.get('/{user_id}', response_model=UserResponse)
async def get_user(user_id: int):
    try:
        return fake_db["users"][user_id]
    except KeyError:
        return {"error": f"User {user_id} not found"}

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    global id
    id += 1
    fake_db["users"][id] = user
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def put_user(user_id: int, new_user_data:UserUpdate):
    try:
        new_user = fake_db["users"][user_id]
    except KeyError:
        return {"error": f"User {user_id} not found"}
    new_user.update(new_user_data.model_dump())
    return new_user

@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int):
    try:
        user = fake_db["users"][user_id]
        del fake_db["users"][user_id]
        return user
    except KeyError:
        return {"error": f"User {user_id} not found"}