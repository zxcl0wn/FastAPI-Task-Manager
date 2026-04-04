from fastapi import APIRouter
from ..schemas import UserCreate, UserUpdate, UserResponse
from typing import List
from ..services import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=List[UserResponse])
async def get_users():
    service = UserService(fake_db)
    return service.get_all()

@router.get('/{user_id}', response_model=UserResponse)
async def get_user(user_id: int):
    service = UserService(fake_db)
    return service.get_by_id(user_id)

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    service = UserService(fake_db)
    return service.create(user.model_dump())

@router.put("/{user_id}", response_model=UserResponse)
async def put_user(user_id: int, new_user_data: UserUpdate):
    service = UserService(fake_db)
    return service.update(user_id, new_user_data.model_dump())

@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int):
    service = UserService(fake_db)
    return service.delete(user_id)