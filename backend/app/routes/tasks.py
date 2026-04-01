from fastapi import APIRouter, HTTPException
from ..database import fake_db
from ..models import TaskCreate, TaskUpdate, TaskResponse
from typing import List


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/", response_model=List[TaskResponse])
async def get_tasks():
    return list(fake_db["tasks"].values())

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    try:
        return fake_db["tasks"][task_id]
    except:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@router.post("/", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    id = len(fake_db["tasks"])+1
    new_task = {'id': id, **task.model_dump()}
    fake_db["tasks"][id] = new_task
    return new_task

@router.put("/{task_id}", response_model=TaskResponse)
async def put_task(task_id: int, new_task_data:TaskUpdate):
    try:
        new_task = fake_db["tasks"][task_id]
        new_task.update(new_task_data.model_dump())
        return new_task
    except:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@router.delete("/{task_id}")
async def delete_task(task_id: int):
    try:
        task = fake_db["tasks"][task_id]
        del fake_db["tasks"][task_id]
        return task
    except:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")