from datetime import datetime

from pydantic import BaseModel


class CategoryData(BaseModel):
    name: str
    created_at: datetime


class CategoryRequest(CategoryData):
    class Config:
        from_attributes = True


class CategoryResponse(CategoryData):
    id: int
    class Config:
        from_attributes = True