from pydantic import BaseModel

class RegisterSchema(BaseModel):
    email: str
    mobile: str
    password: str


class LoginSchema(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    