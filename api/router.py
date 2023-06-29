from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas
from schema.hash import Hash


def show(id: int, db: Session):
    
    router = db.query(models.Router).filter(models.Router.id == id).first()
    if not router:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Router with id {id} not found"
        )
    return router

def get_resources(db: Session):

    return db.query(models.Router).join(models.Permission).all()


def get_all(db: Session):
 
    return db.query(models.Router).all()




