from fastapi import APIRouter
from ..database import fake_db
from ..models import TaskCreate, TaskUpdate, TaskResponse
from typing import List
from ..services import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=List[TaskResponse])
async def get_tasks():
    service = TaskService(fake_db)
    return service.get_all()

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    service = TaskService(fake_db)
    return service.get_by_id(task_id)

@router.post("/", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    service = TaskService(fake_db)
    return service.create(task.model_dump())

@router.put("/{task_id}", response_model=TaskResponse)
async def put_task(task_id: int, new_task_data:TaskUpdate):
    service = TaskService(fake_db)
    return service.update(task_id, new_task_data.model_dump())

@router.delete("/{task_id}", response_model=TaskResponse)
async def delete_task(task_id: int):
    service = TaskService(fake_db)
    return service.delete(task_id)