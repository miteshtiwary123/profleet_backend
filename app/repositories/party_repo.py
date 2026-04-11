from app.models.party import Party


def create_party(db, data):
    party = Party(**data)
    db.add(party)
    db.commit()
    db.refresh(party)
    return party


def get_party_by_id(db, party_id: int):
    return db.query(Party).filter(Party.id == party_id).first()


def get_parties(db, skip=0, limit=10):
    return db.query(Party).offset(skip).limit(limit).all()


def count_parties(db):
    return db.query(Party).count()


def update_party(db, party, data):
    for key, value in data.items():
        setattr(party, key, value)

    db.commit()
    db.refresh(party)
    return party


def delete_party(db, party):
    db.delete(party)
    db.commit()
    