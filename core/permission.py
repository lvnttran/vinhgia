from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api import permission
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["Permission"], prefix="/api/permission")
get_db = configuration.get_db


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.PermissionShow])
def get_permissionShow(db: Session = Depends(get_db)):
    return permission.get_all(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.PermissionShow)
def get_permission_by_id(id: int, db: Session = Depends(get_db)):
    return permission.show(id, db)

