from pydantic import BaseModel
from typing import Optional

class RegisterSchema(BaseModel):
    email: str
    mobile: str
    password: str
    name: Optional[str] = None
    role: Optional[str] = "user"


class LoginSchema(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
