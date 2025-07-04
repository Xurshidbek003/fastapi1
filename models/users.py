from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from db import Base

class Users(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(50), nullable=False)

    # order = relationship("Orders", back_populates='user')