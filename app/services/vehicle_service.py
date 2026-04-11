from fastapi import HTTPException
from app.models.vehicle import Vehicle
from app.repositories.common_repo import create, get_by_id, get_all, delete


def create_vehicle(db, data):
    return create(db, Vehicle, data.dict())


def get_vehicle(db, vehicle_id):
    vehicle = get_by_id(db, Vehicle, vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle


def get_vehicles(db, skip, limit):
    return get_all(db, Vehicle, skip, limit)


def update_vehicle(db, vehicle_id, data):
    vehicle = get_vehicle(db, vehicle_id)

    for key, value in data.dict(exclude_unset=True).items():
        setattr(vehicle, key, value)

    db.commit()
    return vehicle


def delete_vehicle(db, vehicle_id):
    vehicle = get_vehicle(db, vehicle_id)
    delete(db, vehicle)
