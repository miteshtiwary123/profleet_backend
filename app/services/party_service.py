from fastapi import HTTPException
from app.models.party import Party
from app.repositories.common_repo import create, get_by_id, get_all, delete
from app.repositories.party_repo import search_parties


def create_party(db, data):
    return create(db, Party, data.dict())


def get_party(db, party_id):
    party = get_by_id(db, Party, party_id)
    if not party:
        raise HTTPException(status_code=404, detail="Party not found")
    return party


def get_partys(db, skip, limit):
    return get_all(db, Party, skip, limit)


def update_party(db, party_id, data):
    party = get_party(db, party_id)

    for key, value in data.dict(exclude_unset=True).items():
        setattr(party, key, value)

    db.commit()
    return party


def delete_party(db, party_id):
    party = get_party(db, party_id)
    delete(db, party)


def search_parties_service(db, query: str):
    return search_parties(db, query)
