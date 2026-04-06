from fastapi import HTTPException, status
from ..repositories import UserRepository
from sqlalchemy.orm import Session
from ..schemas.user_schema import UserResponse, UserUpdate, UserCreate


class UserService:
    def __init__(self, db) -> None:
        self.user_repository = UserRepository(db)

    def get_all(self) -> list[UserResponse]:
        users = self.user_repository.get_all()
        return [UserResponse.model_validate(user) for user in users]

    def get_by_id(self, user_id: int) -> UserResponse:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
        return UserResponse.model_validate(user)

    def create(self, user: UserCreate) -> UserResponse:
        existing_users = self.user_repository.get_all()
        for existing_user in existing_users:
            if user.username == existing_user.username:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
        created_user = self.user_repository.create(user.model_dump())
        return UserResponse.model_validate(created_user)

    def update(self, user_id: int, new_user_data: UserUpdate) -> UserResponse:
        updated_user = self.user_repository.update(user_id, new_user_data.model_dump())
        if not updated_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
        return UserResponse.model_validate(updated_user)

    def delete(self, user_id: int) -> UserResponse:
        deleted_user = self.user_repository.delete(user_id)
        if not deleted_user:
            raise HTTPException(status_code=404, detail=f"User {user_id} not found")
        return UserResponse.model_validate(deleted_user)
