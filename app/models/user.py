from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db.base import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    mobile = Column(String, unique=True, index=True)

    # Auth
    password = Column(String)

    # Roles
    role = Column(String, default="user", index=True)  # admin, user, etc.
    is_agent = Column(Boolean, default=False)
    is_owner = Column(Boolean, default=False)
    is_driver = Column(Boolean, default=False)

    # Status
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_locked = Column(Boolean, default=False)

    # Security
    failed_attempts = Column(Integer, default=0)


    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )
