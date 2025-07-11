from sqlalchemy import Column, String, Integer, Date
from db import Base

class Users(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50), nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=False)

