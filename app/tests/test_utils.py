import os
from uuid import UUID

import pytest
from fastapi import HTTPException

from app.data_models import FileInfo
from app.utils import create_dir, get_file_info_by_guid, get_files_from_folder


class TestUtils:
    def test_create_dir(self, settings):
        create_dir()
        print(settings)
        assert os.path.exists(settings.upload_dir)

    @pytest.mark.asyncio
    async def test_get_files_from_folder(self, settings):
        create_dir()
        test_guid = UUID("12345678-1234-5678-1234-567812345678")
        test_file_name = "testfile.txt"
        test_file_path = f"{settings.upload_dir}/{test_guid}--{test_file_name}"
        with open(test_file_path, "w") as f:
            f.write("Test content")
        files = await get_files_from_folder()
        assert len(files) == 1
        assert files[0] == FileInfo(guid=str(test_guid), name=test_file_name)
        os.remove(test_file_path)
        os.rmdir(settings.upload_dir)

    @pytest.mark.asyncio
    async def test_get_file_info_by_guid(self, settings):
        create_dir()
        test_guid = UUID("12345678-1234-5678-1234-567812345678")
        test_file_name = "testfile.txt"
        test_file_path = f"{settings.upload_dir}/{test_guid}--{test_file_name}"
        with open(test_file_path, "w") as f:
            f.write("Test content")
        file_info = await get_file_info_by_guid(test_guid)
        assert file_info == FileInfo(guid=str(test_guid), name=test_file_name)
        os.remove(test_file_path)
        os.rmdir(settings.upload_dir)

    def test_save_file_to_folder(self, settings, client):
        create_dir()
        test_guid = "12345678-1234-5678-1234-567812345678"
        client.post(
            "/api/files",
            files={"file": ("testfile.txt", b"test content")},
            data={"guid": test_guid},
        )
        response = client.get(f"/api/files/{test_guid}")
        assert response.status_code == 200
        test_file_path = f"{settings.upload_dir}/{test_guid}--testfile.txt"
        assert os.path.exists(test_file_path)
        os.remove(test_file_path)
        os.rmdir(settings.upload_dir)

    @pytest.mark.asyncio
    async def test_get_file_info_by_guid_not_found(self, settings):
        create_dir()
        test_guid = UUID("12345678-1234-5678-1234-567812345678")
        try:
            await get_file_info_by_guid(test_guid)
        except HTTPException as e:
            assert e.status_code == 404
        os.rmdir(settings.upload_dir)
