from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session
from ..db.session import get_session
from ..models.super_admin_model import SuperAdmin
from ..crud import super_admin_crud
from ..utils.security import decode_access_token
from ..core.config import settings

security = HTTPBearer()

async def get_current_super_admin(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_session)
) -> SuperAdmin:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Session expired. Please log in again.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = credentials.credentials
    try:
        payload = decode_access_token(
            token,
            settings.ACCESS_TOKEN_SECRET_KEY,
            settings.ACCESS_TOKEN_ALGORITHM
        )
        super_admin_id: int = payload.get("sub")
        if super_admin_id is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception
    super_admin = super_admin_crud.get_super_admin_by_id(db, super_admin_id)
    if super_admin is None:
        raise credentials_exception
    return super_admin