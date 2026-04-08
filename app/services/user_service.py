from fastapi import HTTPException
from app.repositories.user_repo import get_user_by_id, update_user, delete_user, get_users, count_users

def update_user_service(db, user_id, data):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return update_user(db, user, data.dict(exclude_unset=True))


def delete_user_service(db, user_id):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    delete_user(db, user)


def get_all_users_service(db, skip=0, limit=10, filters={}):
    users = get_users(db, skip, limit, filters)
    total = count_users(db, filters)

    return {
        "total": total,
        "users": users
    }
