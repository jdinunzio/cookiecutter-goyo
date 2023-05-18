from datetime import datetime

import pytz
from fastapi import APIRouter

router = APIRouter()
start_time = datetime.now(pytz.UTC)


@router.get("/health/live")
async def get_live() -> dict:
    """Health Live end-point."""
    return {
        "status": "ok",
        "start_time": start_time.isoformat(),
        "uptime": str(datetime.now(pytz.UTC) - start_time),
    }


@router.get("/health/ready")
async def get_ready() -> dict:
    """Health Ready end-point."""
    return {
        "status": "ok",
        "start_time": start_time.isoformat(),
        "uptime": str(datetime.now(pytz.UTC) - start_time),
    }
