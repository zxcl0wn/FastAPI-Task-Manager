class UserRepository:
    def __init__(self, db) -> None:
        self.db = db["users"]

    def get_all(self) -> list:
        return list(self.db.values())

    def get_by_id(self, user_id: int) -> dict|None:
        return self.db.get(user_id)

    def create(self, user: dict) -> dict:
        id = len(self.db) + 1
        new_user = {"id": id, **user}
        self.db[id] = new_user
        return new_user

    def update(self, user_id: int, new_user_data: dict) -> dict|None:
        new_user = self.db.get(user_id)
        if new_user:
            new_user.update(new_user_data)
            return new_user
        return None

    def delete(self, user_id: int) -> dict|None:
        user = self.db.get(user_id)
        if user:
            del self.db[user_id]
            return user
        return None