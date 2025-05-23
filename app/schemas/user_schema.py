from typing import List
from pydantic import BaseModel, ConfigDict, EmailStr, StringConstraints
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    phone: str = StringConstraints(min_length=7, max_length=20)
    password: str
    role_id: int
    full_name: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "admin",
                    "password": "admin",
                    "email": "admin@example.com",
                    "phone": "+1234567890",
                    "role_id": 1,
                    "full_name": "Admin"
                }
            ]
        }
    }

class UserPublicInfo(BaseModel):
    id: int
    username: str
    role_id: int
    activated: bool
    created_at: datetime
    updated_at: datetime | None = None
    full_name: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "username": "admin",
                    "role_id": 1,
                    "activated": 1,
                    "created_at": "2020-10-15T20:40:10",
                    "updated_at": "2020-10-15T20:45:08",
                    "full_name": "Admin"
                }
            ]
        }
    }

class User(UserPublicInfo):
    model_config = ConfigDict(from_attributes=True)

class UserCreated(UserPublicInfo):
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "username": "admin",
                    "password": "password",
                    "role_id": 1,
                    "activated": 1,
                    "created_at": "2020-10-15T20:40:10",
                    "updated_at": "2020-10-15T20:45:08",
                    "full_name": "Admin"
                }
            ]
        }
    }

class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    role_id: int | None = None
    activated: bool | None = None
    full_name: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "admin",
                    "password": "admin",
                    "role_id": 1,
                    "activated": 1,
                    "full_name": "Admin"
                }
            ]
        }
    }

class UserHashedPassword(UserPublicInfo):
    hashed_password: str

class UserPublicInfoList(BaseModel):
    page: int
    limit: int
    total: int
    users: List[User]

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    phone: str = StringConstraints(min_length=7, max_length=20)
    full_name: str | None = None

    model_config= {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "newuser",
                    "password": "newpassword",
                    "email": "newuser@example.com",
                    "phone": "+1234567890",
                    "full_name": "John Doe"
                }
            ]
        }
    }