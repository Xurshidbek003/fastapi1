from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from db import Base

class Books(Base):

    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    author = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)

    # order_item = relationship('OrderItems', back_populates='book')