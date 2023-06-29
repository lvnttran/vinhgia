from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates


from database import configuration
from schema import schemas
from schema.oa2 import get_current_user
from starlette.responses import HTMLResponse
from fastapi import Request

router = APIRouter(tags=["HOME UI"], prefix="")
get_db = configuration.get_db
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
   
    return templates.TemplateResponse("home.html", {"request": request})
