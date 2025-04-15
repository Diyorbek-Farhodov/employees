from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.base.pg_db import get_db
from src.exceptions import NotCategoryException
from src.models import Category
from src.schema.category import CategoryRequest

from src.security import get_current_user, has_access

router = APIRouter (prefix='/category', tags=['Category'])






@router.put("/")
@has_access(roles=['super_admin'])
async def change_department(
                                category_id: int,
                                category_data: CategoryRequest,
                                current_user = Depends(get_current_user),
                                db: AsyncSession=Depends(get_db)
                            ):

    result = await db.execute(select(Category).where(Category.id==category_id))
    category =result.scalar_one_or_none()

    if category is None:
        raise NotCategoryException

    for key, value in category_data.dict(exclude_unset=True).items():
        if isinstance(value, datetime) and value.tzinfo:
            value = value.replace(tzinfo=None)
        setattr(category, key, value)
    db.add(category)
    await db.commit()
    await db.refresh(category)


    return f"Department '{category.name}' muvaffaqiyali ozgartirildi"