from pydantic import BaseModel
from enum import Enum


class UserCondition(str, Enum):
    NEW: str = "new"
    INTODUCTION_COMPLETED: str = "introductionCompleted"
    PROFILE_CREATED: str = "profileCreated"


class CreateUser(BaseModel):
    id: int
    login: str
    password: str
    username: str|None


class User(BaseModel):
    id: int
    login: str
    password: str
    username: str|None



