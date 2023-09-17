import logging
from uuid import UUID

from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status
from fastapi.responses import FileResponse

from app.config import settings
from app.data_models import FileInfo
from app.utils import get_file_info_by_guid, get_files_from_folder, save_file_to_folder

router = APIRouter()

log = logging.getLogger(__name__)


@router.get("/api/files", tags=["files"], status_code=status.HTTP_200_OK)
async def get_files() -> list[FileInfo]:
    """Get files from server folder.

    Args:

    Returns:
        List of files info.
    """
    files = await get_files_from_folder()
    return files


@router.post("/api/files", tags=["files"], status_code=status.HTTP_201_CREATED)
async def upload(guid: UUID = Form(...), file: UploadFile = File(...)) -> FileInfo:
    """Upload file in server folder.

    Args:
        guid: GUID for uploaded file.
        file: File that need to upload.

    Returns:
        Uploaded file info.
    """
    try:
        await save_file_to_folder(guid, file)
    except HTTPException as ex:
        raise ex

    file_info = await get_file_info_by_guid(guid)

    return file_info


@router.get("/api/files/{guid}", tags=["files"], status_code=status.HTTP_200_OK)
async def download(guid: UUID) -> FileResponse:
    """Download file from server folder.

    Args:
        guid: GUID files in server folder.

    Returns:
        Downloaded file.
    """
    try:
        file_info = await get_file_info_by_guid(guid)
    except HTTPException as ex:
        raise ex

    return FileResponse(
        f"{settings.upload_dir}/{file_info.guid}--{file_info.name}",
        media_type="application/octet-stream",
        filename=file_info.name,
    )
