import pytest
from fastapi.testclient import TestClient

from app.config import Settings
from app.main import app


@pytest.fixture(scope="session")
def settings():
    return Settings()


@pytest.fixture(scope="session")
def client(settings):
    yield TestClient(app)
