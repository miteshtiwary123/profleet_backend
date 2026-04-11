from fastapi import HTTPException
from app.models.owner import Owner
from app.repositories.common_repo import create, get_by_id, get_all, delete


def create_owner(db, data):
    return create(db, Owner, data.dict())


def get_owner(db, owner_id):
    owner = get_by_id(db, Owner, owner_id)
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return owner


def get_owners(db, skip, limit):
    return get_all(db, Owner, skip, limit)


def update_owner(db, owner_id, data):
    owner = get_owner(db, owner_id)

    for key, value in data.dict(exclude_unset=True).items():
        setattr(owner, key, value)

    db.commit()
    return owner


def delete_owner(db, owner_id):
    owner = get_owner(db, owner_id)
    delete(db, owner)
    