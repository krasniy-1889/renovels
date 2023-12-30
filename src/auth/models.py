from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.auth.schemas import UserReadDTO, UserWithPasswordDTO
from src.database import Base

from src.models import MixinORM


class UserORM(Base, MixinORM):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String(128))

    def to_read_model(self) -> UserWithPasswordDTO:
        return UserWithPasswordDTO(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
