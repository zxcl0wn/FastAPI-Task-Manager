from fastapi import HTTPException, status
from ..repositories import UserRepository


class UserService:
    def __init__(self, db) -> None:
        self.user_repository = UserRepository(db)

    def get_all(self) -> list:
        return self.user_repository.get_all()

    def get_by_id(self, user_id: int) -> dict|None:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
        return user

    def create(self, user: dict) -> dict|None:
        existing_users = self.user_repository.get_all()
        for existing_user in existing_users:
            if user["username"] == existing_user["username"]:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
        return self.user_repository.create(user)

    def update(self, user_id: int, new_user_data: dict) -> dict|None:
        updated_user = self.user_repository.update(user_id, new_user_data)
        if not updated_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
        return updated_user

    def delete(self, user_id: int) -> dict|None:
        deleted_user = self.user_repository.delete(user_id)
        if not deleted_user:
            raise HTTPException(status_code=404, detail=f"User {user_id} not found")
        return deleted_user