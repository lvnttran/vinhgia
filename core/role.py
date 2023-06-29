from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api import role
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["Role"], prefix="/api/role")
get_db = configuration.get_db


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.RoleModel])
def get_role(db: Session = Depends(get_db)):
    return role.get_all(db)

@router.get("/allowed", status_code=status.HTTP_200_OK, response_model=List[schemas.RoleModel])
def get_role_allowed(db: Session = Depends(get_db)):
    return role.get_role_allowed_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.RoleShow)
def create_role(request: schemas.Role, db: Session = Depends(get_db)):
    respone = role.create(request, db)
    return respone

@router.put("/", status_code=status.HTTP_202_ACCEPTED)
def update_role(
    request: schemas.RoleShow,
    db: Session = Depends(get_db),
):
    return role.update(request, db)



@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.RoleShow)
def get_role(id: int, db: Session = Depends(get_db)):
    return role.show(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(
    id: int,
    db: Session = Depends(get_db),
):
   
    return role.destroy(id, db)