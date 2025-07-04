from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import database
from functions.books import add_book, update_book
from models.books import Books
from schemas.books import SchemaBook

router = APIRouter()

@router.get('/')
def get_books(db: Session = Depends(database)):
    try:
        return db.query(Books).all()
    except Exception as e:
        raise HTTPException(400, str(e))


@router.post('/')
def create_book(form: SchemaBook, db: Session = Depends(database)):
    try:
        return add_book(form, db)
    except Exception as e:
        raise HTTPException(400, str(e))


@router.put('/')
def update_books(ident: int, form: SchemaBook, db: Session = Depends(database)):
    try:
        return update_book(ident, form, db)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.delete('/')
def delete_books(ident:int, db: Session = Depends(database)):
    try:
        return delete_books(ident, db)
    except Exception as e:
        raise HTTPException(400, str(e))

