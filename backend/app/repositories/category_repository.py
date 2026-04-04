from sqlalchemy.orm import Session
from ..models import Category


class CategoryRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Category]:
        return self.db.query(Category).all()

    def get_by_id(self, category_id: int) -> dict|None:
        # return self.db.query(Category).filter(Category.id==category_id).first()
        # return self.db.query(Category).get(category_id)
        return self.db.get(Category, category_id)

    def create(self, category: dict) -> Category:
        new_category = Category(**category)
        self.db.add(new_category)
        self.db.commit()
        self.db.refresh(new_category)
        return new_category

    def update(self, category_id: int, new_category_data: dict) -> Category|None:
        category = self.db.get(Category, category_id)
        if category:
            for key, value in new_category_data.items():
                if value is not None:
                    setattr(category, key, value)
            self.db.commit()
            self.db.refresh(category)
            return category
        return None


    def delete(self, category_id: int) -> Category|None:
        category = self.db.get(Category, category_id)
        if category:
            self.db.delete(category)
            self.db.commit()
        return None