from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.testing.pickleable import User
from src.base.pg_db import get_db
from src.exceptions import DepartmentException, NotDepartmentException
from src.models import Department
from src.schema.department import DepartmentRequest
from src.security import get_current_user

department_router = APIRouter (prefix='/department', tags=['Department'])



@department_router.delete("/delete")
async def delete_department(department_id: int, current_user = Depends(get_admin_user), db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Department).where(Department.id==department_id))
    department = result.scalar_one_or_none()

    if department is None:
        raise  NotDepartmentException

    await db.delete(department)
    await db.commit()

    print(f"Admin foydalanuvchi {current_user.username} {department.name} bo‘limini ochirdi")


    return "muvafaqqiyatli ochirildi"