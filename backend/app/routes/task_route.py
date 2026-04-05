from fastapi import APIRouter, Depends
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from typing import List
from ..services import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=List[TaskResponse])
async def get_tasks(db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.get_all()

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.get_by_id(task_id)

@router.post("/", response_model=TaskResponse)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.create(task.model_dump())

@router.put("/{task_id}", response_model=TaskResponse)
async def put_task(task_id: int, new_task_data: TaskUpdate, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.update(task_id, new_task_data.model_dump())

@router.delete("/{task_id}", response_model=TaskResponse)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.delete(task_id)