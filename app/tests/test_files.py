import shutil

from fastapi import HTTPException


def test_upload_file(client):
    test_guid = "12345678-1234-5678-1234-567812345678"
    file_name = "testfile.txt"
    response = client.post(
        "/api/files",
        files={"file": (file_name, b"test content")},
        data={"guid": test_guid},
    )
    assert response.status_code == 201
    assert response.json() == {"guid": test_guid, "name": file_name}


def test_download_file(client):
    test_guid = "748b7b70-109d-4e0d-ad33-a312503e9e11"
    client.post(
        "/api/files",
        files={"file": ("testfile.txt", b"Test content")},
        data={"guid": test_guid},
    )

    response = client.get(f"/api/files/{test_guid}")
    assert response.status_code == 200


def test_download_file_not_found(client):
    guid = "748b7b70-109d-4e0d-ad33-a312503e9e16"
    try:
        client.get(f"/api/files/{guid}")
    except HTTPException as e:
        assert e.status_code == 404


def test_get_files(client):
    response = client.get("/api/files")
    assert response.status_code == 200
    response = response.json()
    assert len(response) == 2
    assert response == [
        {"guid": "12345678-1234-5678-1234-567812345678", "name": "testfile.txt"},
        {"guid": "748b7b70-109d-4e0d-ad33-a312503e9e11", "name": "testfile.txt"},
    ]


def test_clear_folder(settings):
    shutil.rmtree(settings.upload_dir)
