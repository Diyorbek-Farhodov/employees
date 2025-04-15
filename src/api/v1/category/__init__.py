from fastapi import APIRouter

category_router = APIRouter(prefix='/category', tags=['Category'])

from src.api.v1.category.delete import router as delete_router
from src.api.v1.category.add import router as add_router
from src.api.v1.category.put import router as put_router
from src.api.v1.category.get import router as get_router



category_router.include_router(delete_router)
category_router.include_router(add_router)
category_router.include_router(put_router)
category_router.include_router(get_router)