from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="Username")


class UserCreate(BaseUser):
    password: str = Field(..., min_length=5, max_length=20, description="Password")


class UserResponse(BaseUser):
    id: int = Field(..., description="User ID")
    password: str

    class Config:
        from_attributes = True


class UserUpdate(BaseUser):
    username: str|None = None
    password: str|None = None
