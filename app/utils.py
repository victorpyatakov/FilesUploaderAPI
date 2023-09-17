import os
from uuid import UUID
import shutil
from fastapi import HTTPException, UploadFile

from app.config import settings
from app.data_models import FileInfo


def create_dir() -> None:
    """Create directory"""
    os.makedirs(settings.upload_dir, exist_ok=True)


async def get_files_from_folder() -> list[FileInfo]:
    """Get list of files from server folder.

    Args:

    Returns:
        List of files info.
    """
    files = []
    for file in os.listdir(settings.upload_dir):
        guid, file_name = file.split("--")
        files.append(FileInfo(guid=guid, name=file_name))
    return files


async def save_file_to_folder(guid: UUID, file: UploadFile) -> None:
    """Save file in server folder.

    Args:
        guid: GUID for save file.
        file: File info.

    Returns:
    """
    try:
        with open(f"{settings.upload_dir}/{guid}--{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception:
        raise HTTPException(
            status_code=422, detail="During saving file something went wrong"
        )


async def get_file_info_by_guid(guid: UUID) -> FileInfo:
    """Get file info by given guid from server folder.

    Args:
        guid: GUID file name for search file in server folder.

    Returns:
        File info with name and GUID.
    """
    file_name, file_guid = "", ""

    for file in os.listdir(settings.upload_dir):
        if str(guid) in file:
            file_guid, file_name = file.split("--")

    if not file_name:
        raise HTTPException(status_code=404, detail="Item not found")

    return FileInfo(guid=file_guid, name=file_name)
