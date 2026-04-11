from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.db.base import Base


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    phone = Column(String)

    pan_number = Column(String)
    pan_image = Column(String)

    aadhar_front = Column(String)
    aadhar_back = Column(String)

    account_number = Column(String)
    ifsc_code = Column(String)
    bank_name = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )
    