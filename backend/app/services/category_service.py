from fastapi import HTTPException, status
from ..repositories import CategoryRepository
from ..schemas.category_schema import CategoryResponse, CategoryCreate, CategoryUpdate
from sqlalchemy.orm import Session


class CategoryService:
    def __init__(self, db: Session) -> None:
        self.category_repository = CategoryRepository(db)


    def get_all(self) -> list[CategoryResponse]:
        categories = self.category_repository.get_all()
        return [CategoryResponse.model_validate(category) for category in categories]


    def get_by_id(self, category_id: int) -> CategoryResponse:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category {category_id} not found")
        return CategoryResponse.model_validate(category)


    def create(self, category: CategoryCreate) -> CategoryResponse:
        existing_categories = self.category_repository.get_all()
        for existing_category in existing_categories:
            if existing_category.title == category.title:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category already exists")

        created_category = self.category_repository.create(category.model_dump())
        return CategoryResponse.model_validate(created_category)


    def update(self, category_id: int, new_category_data: CategoryUpdate) -> CategoryResponse:
        updated_category = self.category_repository.update(category_id, new_category_data.model_dump(exclude_unset=True))
        if not updated_category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category {category_id} not found")
        return CategoryResponse.model_validate(updated_category)


    def delete(self, category_id: int) -> CategoryResponse:
        deleted_category = self.category_repository.delete(category_id)
        if not deleted_category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category {category_id} not found")
        return CategoryResponse.model_validate(deleted_category)