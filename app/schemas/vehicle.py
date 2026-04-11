from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class VehicleCreate(BaseModel):
    vehicle_number: str
    loading_weight: Optional[str]
    type: Optional[str]
    driver_id: int
    owner_id: int


class VehicleUpdate(BaseModel):
    loading_weight: Optional[str]
    type: Optional[str]
    