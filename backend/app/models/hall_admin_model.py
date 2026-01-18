from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from ..models.student_hall_model import StudentHall
    from ..models.super_admin_model import SuperAdmin
    from ..models.student_model import Student

class HallAdmin(SQLModel, table=True):

    __tablename__ = "hall_admins"
    hall_admin_id: str = Field(primary_key=True, index=True, default_factory=lambda: str(uuid.uuid4()), max_length=36)
    hall_admin_email: str = Field(index=True, max_length=100, unique=True)
    hall_admin_contact_number: str = Field(max_length=15)
    hall_admin_hashed_password: str = Field(max_length=255)
    asscociated_hall_id: Optional[str] = Field(default=None, foreign_key="student_halls.hall_id", index=True, max_length=36)
    created_by_super_admin_id: Optional[str] = Field(default=None, foreign_key="super_admins.super_admin_id", index=True, max_length=36)

    # Relationships
    asscociated_hall: Optional["StudentHall"] = Relationship(back_populates="hall_admins")
    created_by_super_admin: Optional["SuperAdmin"] = Relationship(back_populates="hall_admins_created")
    student_accounts_created: List["Student"] = Relationship(back_populates="created_by_hall_admin")