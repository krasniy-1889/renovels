from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import settings


class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    url=settings.DB_URL_psycopg,
    echo=True,
    pool_size=10,
    max_overflow=10,
)

async_session_maker = async_sessionmaker(engine)
