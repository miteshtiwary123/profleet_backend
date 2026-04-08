from pydantic import BaseModel
from typing import Optional, List

class UpdateUserSchema(BaseModel):
    email: Optional[str] = None
    mobile: Optional[str] = None
    role: Optional[str] = None
    is_agent: Optional[bool] = None
    is_owner: Optional[bool] = None
    is_driver: Optional[bool] = None
    is_active: Optional[bool] = None


class UserResponse(BaseModel):
    id: int
    email: str
    mobile: str
    role: str
    is_active: bool

    class Config:
        from_attributes = True


class UserListResponse(BaseModel):
    total: int
    users: List[UserResponse]
    