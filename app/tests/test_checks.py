import pytest


@pytest.mark.asyncio
async def test_health_check(settings, client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Status": "Ok!"}
