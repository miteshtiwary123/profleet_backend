from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user

from app.schemas.driver import DriverCreate, DriverUpdate
from app.services.driver_service import (
    create_driver, get_driver, get_drivers,
    update_driver, delete_driver
)

router = APIRouter()


@router.post("/")
def create_driver_api(data: DriverCreate, db: Session = Depends(get_db)):
    return create_driver(db, data)


@router.get("/")
def get_all_drivers_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_drivers(db, skip, limit)


@router.get("/{driver_id}")
def get_driver_api(driver_id: int, db: Session = Depends(get_db)):
    return get_driver(db, driver_id)


@router.patch("/{driver_id}")
def update_driver_api(driver_id: int, data: DriverUpdate, db: Session = Depends(get_db)):
    return update_driver(db, driver_id, data)


@router.delete("/{driver_id}")
def delete_driver_api(driver_id: int, db: Session = Depends(get_db)):
    delete_driver(db, driver_id)
    return {"message": "Deleted"}
