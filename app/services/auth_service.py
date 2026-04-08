from app.repositories.user_repo import get_user_by_email, create_user
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token
import random
from fastapi import HTTPException

fake_otp_store = {}

def register_user(db, data):
    existing_user = get_user_by_email(db, data.email)
    if existing_user:
        raise Exception("User already exists")

    data.password = hash_password(data.password)
    user = create_user(db, data.dict())
    return user


def login_user(db, data):
    user = get_user_by_email(db, data.email)
    if not user:
        raise Exception("Invalid credentials")

    if not verify_password(data.password, user.password):
        raise Exception("Invalid credentials")

    access = create_access_token({"sub": str(user.id)})
    refresh = create_refresh_token({"sub": str(user.id)})

    return access, refresh


def forgot_password(db, email: str):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    otp = str(random.randint(100000, 999999))
    fake_otp_store[email] = otp

    print("OTP:", otp)
    return True


def reset_password(db, email: str, otp: str, new_password: str):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if fake_otp_store.get(email) != otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    user.password = hash_password(new_password)
    db.commit()
    