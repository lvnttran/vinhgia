from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api import workshop
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router = APIRouter(tags=["Workshop"], prefix="/api/workshop")
get_db = configuration.get_db


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.WorkshopShow])
def get_workshop(db: Session = Depends(get_db)):
    return workshop.get_all(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.WorkshopShow)
def get_workshop_by_id(id: int, db: Session = Depends(get_db)):
    return workshop.show(id, db)

