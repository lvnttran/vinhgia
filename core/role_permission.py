from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api import role_permission
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["Role Permisssion"], prefix="/api/rolepermisssion")
get_db = configuration.get_db


# @router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.RoleShow])
# def get_role(db: Session = Depends(get_db)):
#     return role.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.RolePermissionShow)
def create_role(request: schemas.RolePermission, db: Session = Depends(get_db)):
    respone = role_permission.create(request, db)
    return respone

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=List[schemas.RolePermission])
def get_all_rolepermission_by_role_id(id: int, db: Session = Depends(get_db)):
    return role_permission.show(id, db)

@router.put("/", status_code=status.HTTP_202_ACCEPTED)
def update_role(
    request: schemas.RolePermissionUpdate,
    db: Session = Depends(get_db),
):
    return role_permission.update(request, db)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(
    request: schemas.RolePermission,
    db: Session = Depends(get_db),
):
   
    return role_permission.destroy(request, db)