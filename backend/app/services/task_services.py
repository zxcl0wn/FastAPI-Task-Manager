from fastapi import HTTPException, status
from ..repositories import TaskRepository, UserRepository, CategoryRepository


class TaskService:
    def __init__(self, db):
        self.task_repository = TaskRepository(db)
        self.user_repository = UserRepository(db)
        self.category_repository = CategoryRepository(db)

    def get_all(self) -> list:
        return self.task_repository.get_all()

    def get_by_id(self, task_id: int) -> dict|None:
        task = self.task_repository.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found")
        return task

    def create(self, task: dict) -> dict:
        user = self.user_repository.get_by_id(task["user_id"])
        category = self.category_repository.get_by_id(task["category_id"])
        if not user or not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User or Category not found")

        existing_tasks = self.task_repository.get_all()
        for existing_task in existing_tasks:
            if existing_task["title"] == task["title"]:
                raise HTTPException(status_code=status.HTTP_400_NOT_FOUND, detail="Task already exists")
        return self.task_repository.create(task)

    def update(self, task_id: int, new_task_data: dict) -> dict|None:
        # Проверка на уникальность категории
        if new_task_data["category_id"]:
            category = self.category_repository.get_by_id(new_task_data["category_id"])
            if not category:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Category {new_task_data['category_id']} not found")
        updated_task = self.task_repository.update(task_id, new_task_data)
        if not updated_task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found")
        return updated_task

    def delete(self, task_id: int) -> dict|None:
        deleted_task = self.task_repository.delete(task_id)
        if not deleted_task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found")
        return deleted_task
