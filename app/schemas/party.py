from pydantic import BaseModel
from typing import Optional, List


class PartyCreate(BaseModel):
    trade_name: str
    address: Optional[str]
    gst_number: str


class PartyUpdate(BaseModel):
    trade_name: Optional[str]
    address: Optional[str]


class PartyResponse(BaseModel):
    id: int
    trade_name: str
    address: Optional[str]
    gst_number: str

    class Config:
        from_attributes = True


class PartyListResponse(BaseModel):
    total: int
    parties: List[PartyResponse]
