from sqlalchemy import Column, Integer, ForeignKey, DateTime
from db import Base
from sqlalchemy.orm import relationship


class Orders(Base):

    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    order_date = Column(DateTime, nullable=False)
    total_price = Column(Integer, nullable=False)

    # user = relationship("Users", back_populates='order')

    # order_item = relationship("OrderItems", back_populates='order')


