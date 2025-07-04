from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import database
from models.books import Books
from models.order_items import OrderItems
from models.orders import Orders
from models.users import Users
from schemas.orders import SchemaOrder
from utils.checked import check_ident

router = APIRouter()

@router.get('/')
def get_orders(db: Session = Depends(database)):
    return db.query(Orders).all()

@router.post('/')
def create_order(form: SchemaOrder, db: Session = Depends(database)):
    check_ident(db, Users, form.user_id)
    order = Orders(
        user_id=form.user_id,
        order_date=form.order_date
    )
    db.add(order)
    db.flush()
    total_order_price = 0
    for item in form.items:
        book = db.query(Books).filter(Books.id == item.book_id).first()
        if not book:
            raise HTTPException(404, 'Kitob topilmadi !')
        if book.amount < item.quantity:
            raise HTTPException(400, 'Kitob yetarli emas !')
        total_price = book.price * item.quantity
        total_order_price += total_price
        book.amount -= item.quantity
        order_items = OrderItems(
            order_id=order.id,
            book_id=item.book_id,
            quantity=item.quantity,
            total_price=total_price
        )
        db.add(order_items)
        db.commit()
    order.total_price = total_order_price
    db.add(order)
    db.commit()
    return {'message': 'Buyurtma qabul qilindi'}