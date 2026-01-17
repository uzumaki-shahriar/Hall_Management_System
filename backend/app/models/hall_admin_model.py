from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
import uuid

class HallAdmin(SQLModel, table=True):

    __tablename__ = "hall_admins"
    hall_admin_id: str = Field(primary_key=True, index=True, default_factory=lambda: str(uuid.uuid4()))
    hall_admin_email: str = Field(index=True, max_length=100, unique=True)
    hall_admin_contact_number: str = Field(max_length=15)
    hall_admin_hashed_password: str = Field(max_length=255)

    # Relationships