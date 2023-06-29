from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema.hash import Hash


def show(id: int, db: Session):
    
    workshop = db.query(models.Workshop).filter(models.Workshop.id == id).first()
    if not workshop:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Workshop with id {id} not found"
        )
    return workshop


def get_all(db: Session):
 
    return db.query(models.Workshop).all()



