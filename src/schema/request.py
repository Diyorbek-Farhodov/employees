from pydantic import BaseModel
from typing_extensions import Optional


class RequestData(BaseModel):
    device_id: Optional[int]=None
    message: str

class RequestCreateRequest(RequestData):
    class Config:
        from_attributes = True


class RequestCreateResponse(RequestData):
    od: int
    class Config:
        from_attributes = True