from sqlalchemy.orm import Session
from ..models import Task


class TaskRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Task]:
        return self.db.query(Task).all()

    def get_by_id(self, task_id: int) -> Task|None:
        return self.db.get(Task, task_id)

    def create(self, task: dict) -> Task:
        new_task = Task(**task)
        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)
        return new_task

    def update(self, task_id: int, new_task_data: dict) -> Task|None:
        task = self.db.get(Task, task_id)
        if task:
            for key, value in new_task_data.items():
                if value is not None:
                    setattr(task, key, value)
            self.db.commit()
            self.db.refresh(task)
            return task
        return None

    def delete(self, task_id: int) -> Task|None:
        task = self.db.get(Task, task_id)
        if task:
            self.db.delete(task)
            self.db.commit()
            return task
        return None