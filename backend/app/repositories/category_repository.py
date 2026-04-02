class CategoryRepository:
    def __init__(self, db) -> None:
        self.db = db["categories"]

    def get_all(self) -> list:
        return list(self.db.values())

    def get_by_id(self, category_id: int) -> dict|None:
        return self.db.get(category_id)

    def create(self, category: dict) -> dict:
        id = len(self.db) + 1
        new_category = {'id': id, **category}
        self.db[id] = new_category
        return new_category

    def update(self, category_id: int, new_category_data: dict) -> dict|None:
        new_category = self.db.get(category_id)
        if new_category:
            new_category.update(new_category_data)
            return new_category
        return None

    def delete(self, category_id: int) -> dict|None:
        category = self.db.get(category_id)
        if category:
            del self.db[category_id]
            return category
        return None