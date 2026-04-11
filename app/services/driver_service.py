from fastapi import HTTPException
from app.models.driver import Driver
from app.repositories.common_repo import create, get_by_id, get_all, delete


def create_driver(db, data):
    return create(db, Driver, data.dict())


def get_driver(db, driver_id):
    driver = get_by_id(db, Driver, driver_id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver


def get_drivers(db, skip, limit):
    return get_all(db, Driver, skip, limit)


def update_driver(db, driver_id, data):
    driver = get_driver(db, driver_id)

    for key, value in data.dict(exclude_unset=True).items():
        setattr(driver, key, value)

    db.commit()
    return driver


def delete_driver(db, driver_id):
    driver = get_driver(db, driver_id)
    delete(db, driver)
    