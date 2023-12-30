from datetime import datetime, timedelta
from re import S

from jose import jwt
from loguru import logger
from src.auth.repository import UserRepository
from passlib.context import CryptContext
from src.auth.services.user import UserService

from src.utils.unitofwork import UnitOfWork

from src.config import settings


class AuthService:
    def __init__(self):
        self.uow = UnitOfWork()
        self.user_service = UserService()
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def _get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return encoded_jwt

    async def authenticate_user(self, username: str, password: str):
        logger.debug('authenticating user "{}" with password "{}"', username, password)
        user = await self.user_service.find_by_username(username)
        logger.debug('user "%s" found: %s', username, user)
        if not user:
            return False
        if not self._verify_password(password, user.password):
            return False
        return user
