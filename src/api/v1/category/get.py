
from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.base.pg_db import get_db
from src.exceptions import NotCategoryException
from src.models import Category
from src.security import get_current_user, has_access

router = APIRouter (prefix='/category', tags=['Category'])




@router.get("/")
@has_access(roles=['super_admin'])
async def get_department(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):

    result = await db.execute(select(Category))
    category = result.scalars().all()

    if category is None:
        raise NotCategoryException

    return category
