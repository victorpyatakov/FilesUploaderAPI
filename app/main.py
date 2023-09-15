import logging
import os
import shutil
from uuid import UUID

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import FileResponse

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

log = logging.getLogger(__name__)

app = FastAPI()


@app.get("/api/files")
async def get_files():
    response = []
    for file in os.listdir(UPLOAD_DIR):
        guid, file_name = file.split("--")
        response.append({
            "guid": guid,
            "file_name": file_name
        })
    return response


@app.post("/api/file")
async def upload(guid: UUID = Form(...), file: UploadFile = File(...)):
    with open(f"{UPLOAD_DIR}/{guid}--{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"username": "name"}


@app.get("/api/file")
async def download(guid: UUID):
    log.info(guid)

    file_name = None
    for file in os.listdir(UPLOAD_DIR):
        if str(guid) in file:
            file_name = file

    if file_name:
        return FileResponse(f"{UPLOAD_DIR}/{file_name}",
                            media_type="application/octet-stream",
                            filename=file_name.split(str(guid))[1],
                            )
    else:
        return {"error": "No such file in given guid"}
