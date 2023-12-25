from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings

sync_engine = create_engine(
    url=settings.DB_URL_psycopg,
    echo=True,
    pool_size=10,
    max_overflow=10,
)

async_engine = create_async_engine(
    url=settings.DB_URL_psycopg,
    echo=True,
    pool_size=10,
    max_overflow=10,
)

session_factory = sessionmaker(sync_engine)


class Base(DeclarativeBase):
    pass
