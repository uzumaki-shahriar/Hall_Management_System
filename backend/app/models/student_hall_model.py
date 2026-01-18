from typing import Optional, TYPE_CHECKING, List
from ..models.hall_admin_model import HallAdmin
from ..models.super_admin_model import SuperAdmin
from sqlmodel import Field, SQLModel, Relationship
from decimal import Decimal
import uuid

class StudentHall(SQLModel, table=True):

    __tablename__ = "student_halls"

    hall_id: str = Field(primary_key=True, index=True, default_factory=lambda: str(uuid.uuid4()), max_length=36)
    hall_name: str = Field(index=True, max_length=100)
    associated_university_name: str = Field(index=True, max_length=150)
    hall_dinning_fee: Decimal = Field(default=Decimal("0.00"), sa_column_kwargs={"precision": 10, "scale": 2})
    total_rooms: int = Field(default=0)
    created_by_super_admin_id: Optional[str] = Field(default=None, foreign_key="super_admins.super_admin_id", index=True, max_length=36)
    

    # Relationships
    hall_admins: List["HallAdmin"] = Relationship(back_populates="asscociated_hall")
    creator_super_admin: Optional[SuperAdmin] = Relationship(back_populates="created_halls")
    
