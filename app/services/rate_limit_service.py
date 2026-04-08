from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from app.models.rate_limit import RateLimit

LIMIT = 5  # 5 requests
WINDOW = 60  # seconds

def check_rate_limit(db, key: str):
    record = db.query(RateLimit).filter(RateLimit.key == key).first()

    now = datetime.now(timezone.utc)

    if not record:
        record = RateLimit(key=key, count=1)
        db.add(record)
        db.commit()
        return

    if (now - record.created_at).seconds > WINDOW:
        record.count = 1
        record.created_at = now
    else:
        record.count += 1

    if record.count > LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests")

    db.commit()
    