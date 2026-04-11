from pydantic import BaseModel
from typing import Optional


class DriverCreate(BaseModel):
    name: str
    licence: str
    phone: Optional[str]


class DriverUpdate(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    