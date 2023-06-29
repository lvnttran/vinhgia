from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api import role_user
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["Role User"], prefix="/api/roleuser")
get_db = configuration.get_db


# @router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.RoleShow])
# def get_role(db: Session = Depends(get_db)):
#     return role.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.RoleUserShow)
def create_role_user(request: schemas.RoleUser, db: Session = Depends(get_db)):
    respone = role_user.create(request, db)
    return respone

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=List[schemas.RoleUserShow])
def get_all_role_user_by_user_id(id: int, db: Session = Depends(get_db)):
    return role_user.show(id, db)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(
    request: schemas.RoleUser,
    db: Session = Depends(get_db),
):
   
    return role_user.destroy(request, db)