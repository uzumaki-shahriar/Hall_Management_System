from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
import uuid

class SuperAdmin(SQLModel, table=True):

    __tablename__ = "super_admins"
    super_admin_id: str = Field(primary_key=True, index=True, default_factory=lambda: str(uuid.uuid4()))
    super_admin_email: str = Field(index=True, max_length=100, unique=True)
    super_admin_name: Optional[str] = Field(default=None, max_length=100, nullable=True)
    super_admin_hashed_password: str = Field(max_length=255)

    # Relationships
