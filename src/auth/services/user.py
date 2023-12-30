from re import A
from typing import Annotated

from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from loguru import logger
from starlette import status
from src.auth.schemas import TokenData, UserCreateDTO, UserReadDTO
from src.utils.unitofwork import IUnitOfWork, UnitOfWork
from src.auth.constants import oauth2_scheme
from src.config import settings


class UserService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_user(self, user: UserCreateDTO, uow: IUnitOfWork):
        async with uow:
            user.password = self.get_password_hash(user.password)
            user = await uow.users.create(user)  # type: ignore
            return user

    async def get_users(self, uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()  # type: ignore
            return users

    async def find_by_username(self, username: str, uow: IUnitOfWork):
        logger.debug('finding user "{}"', username)
        async with uow:
            return await self.uow.users.find_by_username(username)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")  # type: ignore
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await UserService().find_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
