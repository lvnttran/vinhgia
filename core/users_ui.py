from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from database import configuration
from starlette.responses import HTMLResponse
from fastapi import Request

router = APIRouter(tags=["USERS UI"], prefix="/users")
get_db = configuration.get_db
templates = Jinja2Templates(directory="templates")



@router.get("/groups", response_class=HTMLResponse)
async def index(request: Request):
   
    return templates.TemplateResponse("groups.html", {"request": request})

@router.get("/roles", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("rolepermission.html", {"request": request})

