from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.db.base import Base


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    licence = Column(String, nullable=False)
    phone = Column(String)

    aadhar_front = Column(String)
    aadhar_back = Column(String)
    licence_photo = Column(String)
    pan_card_photo = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )
    