from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import configuration
from models import models
from schema import schemas
from schema.hash import Hash
from schema.token import create_access_token
from schema.oa2 import get_current_user
import json
router = APIRouter(prefix="/api/login", tags=["Authentication"])


@router.post("/")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(configuration.get_db),
):
    """
    Login user
    Args:
        request (OAuth2PasswordRequestForm, optional): OAuth2PasswordRequestForm.
        db (Session, optional): Session. Defaults to Depends(configuration.get_db).
    Raises:
        HTTPException: 401 Unauthorized
        HTTPException: 404 Not Found
    Returns:
        Hash: Hash
    """
    user: schemas.User = db.query(models.User).filter(
        models.User.user_email == request.username
    ).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )

    if not Hash.verify(user.user_pass, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password"
        )

    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.user_email})

    # generate JWT token and return
    return {"access_token": f'{access_token}', "token_type": "bearer"}


@router.get("/check_token")
def check_token(
    current_user: schemas.User = Depends(get_current_user),
):

    return {"status": 'success'}