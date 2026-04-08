from app.models.token_blacklist import TokenBlacklist
from datetime import datetime, timezone

def add_blacklist_token(db, token: str, exp):
    expires_at = datetime.fromtimestamp(exp, tz=timezone.utc)

    entry = TokenBlacklist(
        token=token,
        expires_at=expires_at
    )
    db.add(entry)
    db.commit()


def is_token_blacklisted(db, token: str):
    entry = db.query(TokenBlacklist).filter(
        TokenBlacklist.token == token
    ).first()

    if not entry:
        return False

    # auto cleanup logic
    if entry.expires_at < datetime.now(timezone.utc):
        db.delete(entry)
        db.commit()
        return False

    return True
