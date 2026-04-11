from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user

from app.schemas.vehicle import VehicleCreate, VehicleUpdate
from app.services.vehicle_service import (
    create_vehicle, get_vehicle, get_vehicles,
    update_vehicle, delete_vehicle
)

router = APIRouter()


@router.post("/")
def create_vehicle_api(data: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle(db, data)


@router.get("/")
def get_all_vehicles_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_vehicles(db, skip, limit)


@router.get("/{vehicle_id}")
def get_vehicle_api(vehicle_id: int, db: Session = Depends(get_db)):
    return get_vehicle(db, vehicle_id)


@router.patch("/{vehicle_id}")
def update_vehicle_api(vehicle_id: int, data: VehicleUpdate, db: Session = Depends(get_db)):
    return update_vehicle(db, vehicle_id, data)


@router.delete("/{vehicle_id}")
def delete_vehicle_api(vehicle_id: int, db: Session = Depends(get_db)):
    delete_vehicle(db, vehicle_id)
    return {"message": "Deleted"}
