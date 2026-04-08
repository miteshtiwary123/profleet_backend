from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.schemas.auth import RegisterSchema, LoginSchema
from app.schemas.user import UpdateUserSchema, UserListResponse

from app.services.auth_service import (
    register_user, login_user,
    forgot_password, reset_password
)
from app.services.user_service import (
    update_user_service, delete_user_service, get_all_users_service
)
from app.services.audit_service import log_action
from app.services.rate_limit_service import check_rate_limit

from app.repositories.token_repo import add_blacklist_token

from app.api.deps import get_current_user, get_current_user_token
from app.db.session import get_db

router = APIRouter()


@router.post("/register")
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    check_rate_limit(db, f"register:{data.email}")

    user = register_user(db, data)
    return {"message": "User created", "user_id": user.id}


@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    check_rate_limit(db, f"login:{data.email}")

    access, refresh = login_user(db, data)
    return {"access_token": access, "refresh_token": refresh}


@router.post("/logout")
def logout(
    data=Depends(get_current_user_token),
    db: Session = Depends(get_db)
):
    token, payload = data
    exp = payload.get("exp")

    add_blacklist_token(db, token, exp)
    return {"message": "Logged out successfully"}


# 🔐 ADMIN ONLY
@router.patch("/user/{user_id}")
def update_user_api(
    user_id: int,
    data: UpdateUserSchema,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    user = update_user_service(db, user_id, data)

    log_action(db, current_user.id, "UPDATE_USER", user_id)

    return {"message": "User updated"}


@router.delete("/user/{user_id}")
def delete_user_api(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    delete_user_service(db, user_id)

    log_action(db, current_user.id, "DELETE_USER", user_id)

    return {"message": "User deleted"}


@router.post("/forgot-password")
def forgot_password_api(data, db: Session = Depends(get_db)):
    forgot_password(db, data.email)
    return {"message": "OTP sent (mock)"}


@router.post("/reset-password")
def reset_password_api(data, db: Session = Depends(get_db)):
    reset_password(db, data.email, data.otp, data.new_password)
    return {"message": "Password reset successful"}


@router.get("/users", response_model=UserListResponse)
def get_users_api(
    skip: int = 0,
    limit: int = 10,
    role: Optional[str] = None,
    is_active: Optional[bool] = None,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # 🔐 Admin only
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    filters = {
        "role": role,
        "is_active": is_active
    }

    data = get_all_users_service(db, skip, limit, filters)

    return data
