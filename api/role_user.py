from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from api import role, user
from schema import schemas
from schema.hash import Hash


def create(request: schemas.RoleUser, db: Session):
    role_ = role.show(id=request.role_id, db=db)
    user_ = user.show(id=request.user_id, db=db)
    roleuser = db.query(models.RoleUser).filter(
        models.RoleUser.role_id == role_.id and models.RoleUser.user_id == user_.user_id).first()
    if roleuser:
        return roleuser
    new_roleuser = models.RoleUser(role_id=role_.id, user_id= user_.user_id)
    db.add(new_roleuser)
    db.commit()
    db.refresh(new_roleuser)
    return new_roleuser


def show(id: int, db: Session):
    roleusers = db.query(models.RoleUser).filter(models.RoleUser.user_id == id).all()
    return roleusers


def destroy(request: schemas.RoleUser, db: Session):
    roleuser = db.query(models.RoleUser).filter(
        models.RoleUser.role_id == request.role_id and models.RoleUser.user_id == request.user_id)

    if not roleuser.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"RoleUser type with id {request} not found.",
        )
    roleuser.delete(synchronize_session=False)
    db.commit()
    return


