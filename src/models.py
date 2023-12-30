from datetime import datetime
from sqlalchemy import Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declared_attr


class MixinORM:
    @declared_attr  # type: ignore
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, sort_order=-1)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), sort_order=98
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now(), sort_order=99
    )
