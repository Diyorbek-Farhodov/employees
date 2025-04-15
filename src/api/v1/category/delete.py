
from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.base.pg_db import get_db
from src.exceptions import NotCategoryException
from src.models import Category
from src.security import get_current_user, has_access

router = APIRouter (prefix='/category', tags=['Category'])



@router.delete("/delete")
@has_access(roles=['super_admin'])
async def delete_department(category_id: int, current_user = Depends(get_current_user), db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Category).where(Category.id==category_id))
    category = result.scalar_one_or_none()

    if category is None:
        raise  NotCategoryException

    await db.delete(category)
    await db.commit()




    return "muvafaqqiyatli ochirildi"