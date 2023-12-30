from loguru import logger
from sqlalchemy import select
from src.auth.models import UserORM
from src.auth.schemas import UserReadDTO, UserWithPasswordDTO
from src.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = UserORM

    async def find_by_username(self, username: str) -> UserWithPasswordDTO:
        query = select(UserORM).where(UserORM.username == username)
        res = await self.session.execute(query)
        # res = [row.to_read_model() for row in res.one()]
        logger.debug("find_by_username: query result: {}", res)
        return res.scalar_one().to_read_model()

    async def add_one(self, data: dict) -> UserReadDTO:
        return await super().add_one(data)
