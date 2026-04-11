from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user

from app.schemas.owner import OwnerCreate, OwnerUpdate
from app.services.owner_service import (
    create_owner, get_owner, get_owners,
    update_owner, delete_owner
)

router = APIRouter()


@router.post("/")
def create_owner_api(data: OwnerCreate, db: Session = Depends(get_db)):
    return create_owner(db, data)


@router.get("/")
def get_all_owners_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_owners(db, skip, limit)


@router.get("/{owner_id}")
def get_owner_api(owner_id: int, db: Session = Depends(get_db)):
    return get_owner(db, owner_id)


@router.patch("/{owner_id}")
def update_owner_api(owner_id: int, data: OwnerUpdate, db: Session = Depends(get_db)):
    return update_owner(db, owner_id, data)


@router.delete("/{owner_id}")
def delete_owner_api(owner_id: int, db: Session = Depends(get_db)):
    delete_owner(db, owner_id)
    return {"message": "Deleted"}
