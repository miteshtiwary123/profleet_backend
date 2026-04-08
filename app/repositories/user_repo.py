from app.models.user import User
from datetime import datetime, timezone

def get_user_by_email(db, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db, user_data):
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db, user, update_data: dict):
    for key, value in update_data.items():
        setattr(user, key, value)

    # Force update timestamp (recommended)
    user.updated_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db, user):
    db.delete(user)
    db.commit()


def get_users(db, skip: int = 0, limit: int = 10, filters: dict = {}):
    query = db.query(User)

    if filters.get("role"):
        query = query.filter(User.role == filters["role"])

    if filters.get("is_active") is not None:
        query = query.filter(User.is_active == filters["is_active"])

    return query.offset(skip).limit(limit).all()


def count_users(db, filters: dict = {}):
    query = db.query(User)

    if filters.get("role"):
        query = query.filter(User.role == filters["role"])

    if filters.get("is_active") is not None:
        query = query.filter(User.is_active == filters["is_active"])

    return query.count()
