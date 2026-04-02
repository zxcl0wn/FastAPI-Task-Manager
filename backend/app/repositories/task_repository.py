class TaskRepository:
    def __init__(self, db) -> None:
        self.db = db["tasks"]

    def get_all(self) -> list:
        return list(self.db.values())

    def get_by_id(self, task_id: int) -> dict|None:
        return self.db.get(task_id)

    def create(self, task: dict) -> dict:
        id = len(self.db) + 1
        new_task = {'id': id, **task}
        self.db[id] = new_task
        return new_task

    def update(self, task_id: int, new_task_data: dict) -> dict|None:
        new_task = self.db.get(task_id)
        if new_task:
            new_task.update(new_task_data)
            return new_task
        return None

    def delete(self, task_id: int) -> dict|None:
        task = self.db.get(task_id)
        if task:
            del self.db[task_id]
            return task
        return None