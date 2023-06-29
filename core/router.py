from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api import router as rt
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user

router= APIRouter(tags=["Router"], prefix="/api/router")
get_db = configuration.get_db


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.RouterShow])
def get_router(db: Session = Depends(get_db)):
    return rt.get_all(db)

@router.get("/resources", status_code=status.HTTP_200_OK, response_model=List[schemas.RouterModel])
def get_router(db: Session = Depends(get_db)):
    return rt.get_resources(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.RouterShow)
def get_router(id: int, db: Session = Depends(get_db)):
    return rt.show(id, db)