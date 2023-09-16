import os
import shutil
from uuid import UUID
from fastapi import File
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
        files.append(FileInfo(**{
            "guid": guid,
            "name": file_name
        }))
    return files


async def save_file_to_folder(guid: UUID, file: File) -> None:
    """Save file in server folder.

    Args:
        guid: GUID for save file.
        file: File info.

    Returns:
    """
    with open(f"{settings.upload_dir}/{guid}--{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


async def get_file_info_by_guid(guid: UUID) -> FileInfo:
    """Get file info by given guid from server folder.

    Args:
        guid: GUID file name for search file in server folder.

    Returns:
        File info with name and GUID.
    """
    file_name = None

    for file in os.listdir(settings.upload_dir):
        if str(guid) in file:
            guid, file_name = file.split("--")

    return FileInfo(**{
        "guid": guid,
        "name": file_name
    })
