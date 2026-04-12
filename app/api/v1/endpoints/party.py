from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user

from app.schemas.party import PartyCreate, PartyUpdate
from app.services.party_service import (
    create_party, get_party, get_partys,
    update_party, delete_party, search_parties_service
)

router = APIRouter()


@router.post("/")
def create_party_api(data: PartyCreate, db: Session = Depends(get_db)):
    return create_party(db, data)


@router.get("/")
def get_all_partys_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_partys(db, skip, limit)


@router.get("/search")
def search_party_api(
    query: str,
    db: Session = Depends(get_db)
):
    results = search_parties_service(db, query)

    return {
        "message": "Search results",
        "count": len(results),
        "data": results
    }


@router.get("/{party_id}")
def get_party_api(party_id: int, db: Session = Depends(get_db)):
    return get_party(db, party_id)


@router.patch("/{party_id}")
def update_party_api(party_id: int, data: PartyUpdate, db: Session = Depends(get_db)):
    return update_party(db, party_id, data)


@router.delete("/{party_id}")
def delete_party_api(party_id: int, db: Session = Depends(get_db)):
    delete_party(db, party_id)
    return {"message": "Deleted"}
