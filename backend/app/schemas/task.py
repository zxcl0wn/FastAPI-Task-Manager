from pydantic import BaseModel, Field


class BaseTask(BaseModel):
    title: str = Field(..., min_length=5, max_length=30, description="Task title")
    description: str|None = Field(None, description="Task description")

class TaskCreate(BaseTask):
    category_id: int = Field(..., description="Category ID")
    user_id: int = Field(..., description="User ID")

class TaskResponse(BaseTask):
    id: int = Field(..., description="Task ID")
    category_id: int
    user_id: int

class TaskUpdate(BaseTask):
    title: str|None = None
    description: str|None = None
    category_id: int|None = None