from pydantic import BaseModel

# Users:
class BaseUser(BaseModel):
    username: str

class UserCreate(BaseUser):
    password: str

class UserResponse(BaseUser):
    id: int
    password: str

class UserUpdate(BaseUser):
    username: str|None = None
    password: str|None = None


# Tasks
class BaseTask(BaseModel):
    title: str
    description: str|None = None

class TaskCreate(BaseTask):
    category_id: int
    user_id: int

class TaskResponse(BaseTask):
    id: int
    category_id: int
    user_id: int

class TaskUpdate(BaseTask):
    title: str|None = None
    description: str|None = None
    category_id: int|None = None


# Categories
class BaseCategory(BaseModel):
    title: str

class CategoryCreate(BaseCategory):
    ...

class CategoryResponse(BaseCategory):
    id: int

class CategoryUpdate(BaseCategory):
    title: str|None = None
