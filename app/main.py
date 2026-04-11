from fastapi import FastAPI
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.party import router as party_router
from app.api.v1.endpoints.driver import router as driver_router
from app.api.v1.endpoints.owner import router as owner_router
from app.api.v1.endpoints.vehicle import router as vehicle_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(party_router, prefix="/party", tags=["Party"])
app.include_router(driver_router, prefix="/driver", tags=["Driver"])
app.include_router(owner_router, prefix="/owner", tags=["Owner"])
app.include_router(vehicle_router, prefix="/vehicle", tags=["Vehicle"])
