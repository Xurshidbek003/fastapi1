from models.books import Books
from utils.checked import check_ident


def add_book(form, db):
    book = Books(
        name=form.name,
        author=form.author,
        price=form.price,
        amount=form.amount
    )
    db.add(book)
    db.commit()
    return {'message': "Kitob qo'shildi"}


def update_book(ident, form, db):
    check_ident(db, Books, ident)
    db.query(Books).filter(Books.id==ident).update({
        Books.name: form.name,
        Books.author: form.author,
        Books.price: form.price,
        Books.amount: form.amount
    })
    db.commit()
    return {'message': "Kitob tahrirlandi"}


def delete_book(ident, db):
    check_ident(db, Books, ident)
    db.query(Books).filter(Books.id==ident).delete()
    db.commit()
    return {'message': "Kitob ochirildi"}
