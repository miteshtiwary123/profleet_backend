from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.security import decode_token
from app.repositories.user_repo import get_user_by_id
from app.repositories.token_repo import is_token_blacklisted

security = HTTPBearer()


def get_current_user_token(
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    if is_token_blacklisted(db, token):
        raise HTTPException(status_code=401, detail="Token blacklisted")

    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    return token, payload


def get_current_user(
    db: Session = Depends(get_db),
    data=Depends(get_current_user_token),
):
    _, payload = data

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = get_user_by_id(db, int(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
