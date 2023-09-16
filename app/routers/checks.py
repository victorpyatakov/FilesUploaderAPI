from fastapi import APIRouter

router = APIRouter()


@router.get("/", include_in_schema=False)
async def check_health() -> dict:
    """Check health of application

    Args:

    Returns:
        Info about app state."""
    return {"Status": "Ok!"}
