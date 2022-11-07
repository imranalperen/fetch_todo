from backend.db import Base, engine
from sqlalchemy import Column, Integer, String, Date, UniqueConstraint

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(30), nullable=False, unique=True)
    hashed_password = Column(String(100), nullable=False)
    access_token = Column(String(100))
    access_token_create_date = Column(Date)
    access_token_expire_date = Column(Date)


Base.metadata.create_all(engine)