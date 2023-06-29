from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import models
from api import workshop
from schema import schemas
from schema.hash import Hash


def create(request: schemas.Role, db: Session):
    
    workshop_pr = workshop.show(id=request.workshop_id, db=db)
    new_role = models.Role(name=request.name, workshop_id=workshop_pr.id)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role


def show(id: int, db: Session):
    
    role = db.query(models.Role).filter(models.Role.id == id).first()
    if not role:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Role with id {id} not found"
        )
    return role


def get_all(db: Session):
    return db.query(models.Role).join(models.Workshop).join(models.Factory).all()

def get_role_allowed_all(db: Session):
    subquery = db.query(models.RolePermission.role_id).distinct()
    return db.query(models.Role).filter(models.Role.id.in_(subquery)).all()

def update(request: schemas.RoleShow, db: Session):
  
    role = db.query(models.Role).filter(
        models.Role.id == request.id).first()
    workshop_pr = workshop.show(id=request.workshop_id, db=db)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Floor type with id {id} not found"
        )
    
    role.workshop_id = workshop_pr.id
    role.name = request.name
    db.commit()
    return "updated"

def destroy(id: int, db: Session):
    role = db.query(models.Role).filter(
        models.Role.id == id)

    if not role.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Role type with id {id} not found.",
        )
   
    role.delete(synchronize_session=False)
    db.commit()
    return


