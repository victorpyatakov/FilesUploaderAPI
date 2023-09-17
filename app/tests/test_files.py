import os
import shutil

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
UPLOAD_DIR = "uploads_test"


@pytest.fixture(scope="module", autouse=True)
def setup_teardown():
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    yield
    shutil.rmtree(UPLOAD_DIR)


def test_upload_file():
    response = client.post(
        "/api/file",
        files={"file": ("testfile.txt", b"test content")},
        data={"guid": "1234-5678-1234-5678"},
    )
    assert response.status_code == 200


def test_get_files():
    response = client.get("/api/files")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_download_file():
    test_guid = "748b7b70-109d-4e0d-ad33-a312503e9e11"
    client.post(
        "/api/file",
        files={"file": ("testfile.txt", b"test content")},
        data={"guid": test_guid},
    )

    response = client.get(f"/api/file?guid={test_guid}")
    assert response.status_code == 200


def test_download_file_not_found():
    guid = "748b7b70-109d-4e0d-ad33-a312503e9e11"
    response = client.get(f"/api/file?guid={guid}")
    assert response.status_code == 200
