from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.testing.pickleable import User
from src.base.pg_db import get_db
from src.exceptions import CategoryException
from src.models import Department, Category

from src.security import get_current_user, has_access

router = APIRouter (prefix='/category', tags=['Category'])

@router.post("/add_department")
@has_access(roles=['super_admin'])
async def add_department(name: str, db:AsyncSession = Depends(get_db), current_user:User =  Depends(get_current_user)):


    result = await db.execute(select(Category).where(name==Category.name))
    existing_department = result.scalar_one_or_none()

    if existing_department :
        raise CategoryException

    new_category = Department(name=name)

    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)

    return new_category
