from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api import user
from database import configuration
from schema import schemas
from schema.oa2 import get_current_user
router = APIRouter(tags=["Users"], prefix="/api/users")
get_db = configuration.get_db


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(request: schemas.User, db: Session = Depends(get_db), 
                # current_user: schemas.User = Depends(get_current_user),
                ):
    return user.create(request, db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserShow)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
   
    return user.show(id, db)

# @router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
# def get_users(db: Session = Depends(get_db)):
#     """
#     Get all users
#     Args:
#         db (Session, optional): Database session. Defaults to Depends(get_db).
#     Returns:
#         List[schemas.ShowUser]: List of users
#     """
#     return user.get_all(db)



