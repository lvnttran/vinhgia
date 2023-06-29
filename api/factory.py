from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from schema import schemas
from schema.hash import Hash


def create(request: schemas.Factory, db: Session):
    print(request)
    factory = models.Factory(name=request.name, location=request.location, workshops=[])
    db.add(factory)
    db.commit()
    db.refresh(factory)
    return  factory


def show(id: int, db: Session):
    
    factory = db.query(models.Factory).filter(models.Factory.id == id).first()
    if not factory:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Factory with id {id} not found"
        )
    return factory


def get_all(db: Session):
 
    return db.query(models.Factory).all()

def get_all_full(db: Session):
 
    return db.query(models.Factory).join(models.Workshop).all()

 
def destroy(id: int, db: Session):
    factory_to_delete = db.query(models.Factory).filter(
        models.Factory.id == id)

    if not factory_to_delete.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Factory type with id {id} not found.",
        )
   
    factory_to_delete.delete(synchronize_session=False)
    db.commit()
    return


