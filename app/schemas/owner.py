from pydantic import BaseModel
from typing import Optional


class OwnerCreate(BaseModel):
    name: str
    phone: Optional[str]
    pan_number: Optional[str]


class OwnerUpdate(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    