from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas
from schema.hash import Hash


def show(id: int, db: Session):
    
    permission = db.query(models.Permission).filter(models.Permission.id == id).first()
    if not permission:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Permission with id {id} not found"
        )
    return permission


def get_all(db: Session):
 
    return db.query(models.Permission).all()



