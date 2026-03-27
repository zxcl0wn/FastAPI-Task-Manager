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
    category_id: str
    user_id: str

class TaskResponse(BaseTask):
    id: int
    category_id: str
    user_id: str

class TaskUpdate(BaseTask):
    title: str|None = None
    description: str|None = None
    category_id: str|None = None
    user_id: str|None = None


# Categories
class BaseCategory(BaseModel):
    title: str

class CategoryCreate(BaseCategory):
    password: str

class CategoryResponse(BaseCategory):
    id: int
    password: str

class CategoryUpdate(BaseCategory):
    title: str|None = None
    password: str|None = None