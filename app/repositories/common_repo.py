def create(db, model, data):
    obj = model(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_by_id(db, model, obj_id):
    return db.query(model).filter(model.id == obj_id).first()


def get_all(db, model, skip=0, limit=10):
    return db.query(model).offset(skip).limit(limit).all()


def delete(db, obj):
    db.delete(obj)
    db.commit()
    