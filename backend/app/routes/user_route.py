from fastapi import APIRouter, Depends
from ..schemas.user_schema import UserCreate, UserUpdate, UserResponse
from typing import List
from ..services import UserService
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=List[UserResponse])
async def get_users(db: Session=Depends(get_db)):
    service = UserService(db)
    return service.get_all()

@router.get('/{user_id}', response_model=UserResponse)
async def get_user(user_id: int, db: Session=Depends(get_db)):
    service = UserService(db)
    return service.get_by_id(user_id)

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session=Depends(get_db)):
    service = UserService(db)
    return service.create(user)

@router.put("/{user_id}", response_model=UserResponse)
async def put_user(user_id: int, new_user_data: UserUpdate, db: Session=Depends(get_db)):
    service = UserService(db)
    return service.update(user_id, new_user_data)

@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int, db: Session=Depends(get_db)):
    service = UserService(db)
    return service.delete(user_id)