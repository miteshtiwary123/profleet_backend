from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from datetime import datetime, timezone
from app.db.base import Base


class Party(Base):
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True)

    trade_name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    pincode = Column(String, nullable=True)

    gst_number = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )
    