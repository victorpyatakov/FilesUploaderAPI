from fastapi import FastAPI

from app.routers import files, checks
from app.utils import create_dir

app = FastAPI()

app.include_router(files.router)
app.include_router(checks.router)

create_dir()
