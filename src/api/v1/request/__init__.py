from fastapi import APIRouter


request_router = APIRouter(prefix="/request", tags=['Request'])

from src.api.v1.request.add import router as add_router



request_router.include_router(add_router)