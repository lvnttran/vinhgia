from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from core import factory, workshop, router, permission, role, role_permission, user, role_user, home_ui, users_ui
from database.configuration import engine
from models import models
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VINH GIA",
    description="Website nội bộ của công ty Vinh Gia",
    version="1.0.0"
    
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(factory.router)
app.include_router(workshop.router)
app.include_router(router.router)
app.include_router(permission.router)
app.include_router(role.router)
app.include_router(role_permission.router)
app.include_router(user.router)
app.include_router(role_user.router)
app.include_router(home_ui.router)
app.include_router(users_ui.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='', port=80, reload=True)
