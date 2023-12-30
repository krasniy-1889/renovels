from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Base


class SQLAlchemyRepository:
    model = None | Base

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        query = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(query)
        await self.session.commit()
        return res.scalar_one()

    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
