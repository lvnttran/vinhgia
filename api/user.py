from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas
from schema.hash import Hash


def create(request: schemas.User, db: Session):
   
    hashedPassword = Hash.bcrypt(request.user_pass)
    user = models.User(name=request.name, user_email=request.user_email, user_pass=hashedPassword)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.user_id == id).first()
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return user


# def get_all(db: Session):
  
#     return db.query(models.User).all()