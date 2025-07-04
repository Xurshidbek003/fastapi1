from models.users import Users
from utils.checked import check_ident


def add_user(form, db):
    user = Users(
        **form.dict()
    )
    db.add(user)
    db.commit()
    return {'message': "User qo'shildi"}


def update_user(ident, form, db):
    check_ident(db, Users, ident)
    db.query(Users).filter(Users.id==ident).update({
        Users.name: form.name,
        Users.phone: form.phone,
        Users.address: form.address,
    })
    db.commit()
    return {'message': "User tahrirlandi"}


def delete_user(ident, db):
    check_ident(db, Users, ident)
    db.query(Users).filter(Users.id==ident).delete()
    db.commit()
    return {'message': "User ochirildi"}
