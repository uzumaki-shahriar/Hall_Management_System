from pydantic import BaseModel
from typing import Optional

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

class MessageResponse(BaseModel):
    
    response_code: Optional[int] = None
    message: str
    success: bool

class ErrorResponse(BaseModel):
    detail: str
    code: Optional[int] = None