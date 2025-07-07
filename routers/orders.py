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
def get_orders(ident:int = None, db: Session = Depends(database)):
    if ident:
        orders = db.query(Orders).filter(Orders.id == ident).first()

        all_orders_response = []

        order_items = db.query(OrderItems).filter(OrderItems.order_id == orders.id).all()

        all_orders_response.append({
            "order_id": orders.id,
            "order_date": orders.order_date,
            "total_price": orders.total_price,
            "items": [
                {
                    "book_id": item.book_id,
                    "quantity": item.quantity,
                    "total_price": item.total_price
                }
                for item in order_items
            ]
        })

        return all_orders_response
    else:
        orders = db.query(Orders).all()

        all_orders_response = []

        for order in orders:
            order_items = db.query(OrderItems).filter(OrderItems.order_id == order.id).all()

            all_orders_response.append({
                "order_id": order.id,
                "order_date": order.order_date,
                "total_price": order.total_price,
                "items": [
                    {
                        "book_id": item.book_id,
                        "quantity": item.quantity,
                        "total_price": item.total_price
                    }
                    for item in order_items
                ]
            })

        return all_orders_response


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