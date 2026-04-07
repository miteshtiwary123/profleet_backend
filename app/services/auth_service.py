from app.repositories.user_repo import get_user_by_email, create_user
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token

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
