from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class OrderItems(Base):

    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)

    # order = relationship("Orders", back_populates="order_item")

    # book = relationship("Books", back_populates='order_item')