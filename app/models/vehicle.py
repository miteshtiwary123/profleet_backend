from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone
from app.db.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)

    vehicle_number = Column(String, unique=True, index=True)
    loading_weight = Column(String)
    type = Column(String)

    purchase_date = Column(DateTime(timezone=True))
    purchase_price = Column(String)

    rc_image = Column(String)

    insurance_expiry_date = Column(DateTime(timezone=True))
    puc_expiry_date = Column(DateTime(timezone=True))
    fitness_expiry_date = Column(DateTime(timezone=True))
    tax_expiry_date = Column(DateTime(timezone=True))
    permit_expiry_date = Column(DateTime(timezone=True))
    next_service_due_date = Column(DateTime(timezone=True))

    driver_id = Column(Integer, ForeignKey("drivers.id"))
    owner_id = Column(Integer, ForeignKey("owners.id"))

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )
    