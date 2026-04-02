from fastapi import APIRouter, HTTPException
from ..database import fake_db
from ..models import TaskCreate, TaskUpdate, TaskResponse
from typing import List
from ..repositories.tasks_repository import TaskRepository


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=List[TaskResponse])
async def get_tasks():
    tasks = TaskRepository(fake_db).get_all()
    return tasks

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    task = TaskRepository(fake_db).get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return task


@router.post("/", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    new_task = TaskRepository(fake_db).create(task.model_dump())
    return new_task

@router.put("/{task_id}", response_model=TaskResponse)
async def put_task(task_id: int, new_task_data:TaskUpdate):
    updated_task = TaskRepository(fake_db).update(task_id, new_task_data.model_dump())
    if not updated_task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return updated_task


@router.delete("/{task_id}")
async def delete_task(task_id: int):
    deleted_task = TaskRepository(fake_db).delete(task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return deleted_task
