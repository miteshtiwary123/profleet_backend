from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth import RegisterSchema, LoginSchema
from app.services.auth_service import register_user, login_user
from app.db.session import get_db

router = APIRouter()


@router.post("/register")
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    user = register_user(db, data)
    return {"message": "User created", "user_id": user.id}


@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    access, refresh = login_user(db, data)
    return {
        "access_token": access,
        "refresh_token": refresh
    }
