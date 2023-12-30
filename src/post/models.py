# from sqlalchemy import Integer, Text, String, CheckConstraint
# from sqlalchemy.orm import Mapped, mapped_column
#
# from src.database import Base


# class PostORM(Base):
#     __tablename__ = "posts"
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     title: Mapped[str] = mapped_column(String(300))
#     content: Mapped[str] = mapped_column(Text)
#     likes: Mapped[int] = mapped_column(Integer, CheckConstraint("likes > 0"), default=0)
