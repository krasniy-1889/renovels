from datetime import datetime
from pydantic import BaseModel


# User
class UserBaseDTO(BaseModel):
    class Config:
        from_attributes = True


class UserCreateDTO(UserBaseDTO):
    username: str
    email: str
    password: str


class UserReadDTO(UserBaseDTO):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime


class UserWithPasswordDTO(UserReadDTO):
    password: str


# Token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str
