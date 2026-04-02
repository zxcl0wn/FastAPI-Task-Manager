from fastapi import HTTPException, status
from ..repositories import CategoryRepository


class CategoryService:
    def __init__(self, db) -> None:
        self.category_repository = CategoryRepository(db)

    def get_all(self) -> list:
        return self.category_repository.get_all()

    def get_by_id(self, category_id: int) -> dict|None:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category {category_id} not found")
        return category

    def create(self, category: dict) -> dict:
        existing_categories = self.category_repository.get_all()
        for existing_category in existing_categories:
            if existing_category["title"] == category["title"]:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category already exists")
        return self.category_repository.create(category)

    def update(self, category_id: int, new_category_data: dict) -> dict|None:
        updated_category = self.category_repository.update(category_id, new_category_data)
        if not updated_category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category {category_id} not found")
        return updated_category

    def delete(self, category_id: int) -> dict|None:
        deleted_category = self.category_repository.delete(category_id)
        if not deleted_category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category {category_id} not found")
        return deleted_category