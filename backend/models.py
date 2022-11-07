from db import Base, session, engine
from sqlalchemy import Column, Integer, String

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    email = Column(String(30))
    hashed_password = Column(String(50))


Base.metadata.create_all(engine)