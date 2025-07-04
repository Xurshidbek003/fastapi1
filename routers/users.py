from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import database
from functions.users import add_user, update_user, delete_user
from models.users import Users
from schemas.users import SchemaUser

router = APIRouter()

@router.get('/')
def get_users(db: Session = Depends(database)):
    try:
        return db.query(Users).all()
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post('/')
def create_user(form: SchemaUser, db: Session = Depends(database)):
    try:
        return add_user(form, db)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.put('/')
def update_users(ident: int, form: SchemaUser, db: Session = Depends(database)):
    try:
        return update_user(ident, form, db)
    except Exception as e:
        raise HTTPException(400, str(e))

@router.delete('/')
def delete_users(ident: int, db: Session = Depends(database)):
    try:
        return delete_user(ident, db)
    except Exception as e:
        raise HTTPException(400, str(e))