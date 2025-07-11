from models.users import Users
from routers.auth import get_password_hash
from utils.checked import check_ident


def add_user(form, db):
    user = Users(
        full_name = form.full_name,
        username = form.username,
        password = get_password_hash(form.password),
        birth_date = form.birth_date
    )
    db.add(user)
    db.commit()
    return {'message': "User qo'shildi"}


def delete_user(ident, db):
    check_ident(db, Users, ident)
    db.query(Users).filter(Users.id==ident).delete()
    db.commit()
    return {'message': "User ochirildi"}
