from sqlalchemy import select

from src.base.pg_db import get_db
from src.models import User, Device, Request
from src.schema.request import RequestCreateResponse, RequestCreateRequest
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.security import get_current_user

router = APIRouter(prefix="/requests")


@router.post("/", response_model=RequestCreateResponse)
async def create_device_request(
    request_data: RequestCreateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if request_data.device_id:
        result = await db.execute(
            select(Device).where(Device.id == request_data.device_id)
        )
        device = result.scalars().first()
        if not device:
            raise HTTPException(status_code=404, detail="Qurilma topilmadi")

        if device.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Ushbu qurilmaga murojaat qilish mumkin emas")

