from fastapi import HTTPException, status
from ..repositories import TaskRepository, UserRepository, CategoryRepository
from sqlalchemy.orm import Session
from ..schemas.task_schema import TaskResponse, TaskUpdate, TaskCreate


class TaskService:
    def __init__(self, db: Session):
        self.task_repository = TaskRepository(db)
        self.user_repository = UserRepository(db)
        self.category_repository = CategoryRepository(db)


    def get_all(self) -> list[TaskResponse]:
        tasks = self.task_repository.get_all()
        return [TaskResponse.model_validate(task) for task in tasks]


    def get_by_id(self, task_id: int) -> TaskResponse:
        task = self.task_repository.get_by_id(task_id)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found")
        return TaskResponse.model_validate(task)


    def create(self, task: TaskCreate) -> TaskResponse:
        user = self.user_repository.get_by_id(task.user_id)
        category = self.category_repository.get_by_id(task.category_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User {task.user_id} not found")
        if not category:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Category {task.category_id} not found")

        created_task = self.task_repository.create(task.model_dump())
        return TaskResponse.model_validate(created_task)


    def update(self, task_id: int, new_task_data: TaskUpdate) -> TaskResponse:
        if new_task_data.category_id is not None:
            category = self.category_repository.get_by_id(new_task_data.category_id)
            if not category:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Category {new_task_data.category_id} not found")

        updated_task = self.task_repository.update(task_id, new_task_data.model_dump(exclude_unset=True))
        if not updated_task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found")
        return TaskResponse.model_validate(updated_task)


    def delete(self, task_id: int) -> TaskResponse:
        deleted_task = self.task_repository.delete(task_id)
        if not deleted_task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found")
        return TaskResponse.model_validate(deleted_task)
