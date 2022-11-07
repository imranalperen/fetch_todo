from backend.db import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(30), nullable=False, unique=True)
    hashed_password = Column(String(100), nullable=False)
    access_token = Column(String(100))
    access_token_create_date = Column(DateTime)
    access_token_expire_date = Column(DateTime)


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    todo_body = Column(String(250))
    user_id = Column(Integer, ForeignKey("users.id"))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


Base.metadata.create_all(engine)