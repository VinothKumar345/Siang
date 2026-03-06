# backend/database/models.py
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


    username = Column(String, unique=True)

    email = Column(String, unique=True)

    mobile_number = Column(String)

    hashed_password = Column(String)