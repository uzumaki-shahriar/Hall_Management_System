from typing import Optional, TYPE_CHECKING, List
from sqlmodel import Field, SQLModel, Relationship
from decimal import Decimal


if TYPE_CHECKING:
    from ..models.hall_admin_model import HallAdmin
    from ..models.student_hall_model import StudentHall
    from ..models.feedback_model import Feedback
    from ..models.dinning_data_model import DinningData


class Student(SQLModel, table=True):

    __tablename__ = "students"

    student_id: str = Field(primary_key=True, index=True, max_length=8)
    student_email: str = Field(index=True, max_length=100, unique=True)
    student_name: Optional[str] = Field(default=None, max_length=100, nullable=True)
    student_department: Optional[str] = Field(default=None, max_length=100, nullable=True)
    is_dinning_manager: bool = Field(default=False)
    student_home_address: Optional[str] = Field(default=None, max_length=200, nullable=True)
    student_contact_number: Optional[str] = Field(default=None, max_length=15, nullable=True)
    student_batch: Optional[str] = Field(default=None, max_length=10, nullable=True)
    student_hall_fee: Optional[Decimal] = Field(default=None, nullable=True)
    student_room_number: Optional[int] = Field(default=0, nullable=True)
    student_hashed_password: str = Field(max_length=255)
    created_by_hall_admin_id: Optional[str] = Field(default=None, foreign_key="hall_admins.hall_admin_id", index=True, max_length=36)
    student_hall_id: Optional[str] = Field(default=None, foreign_key="student_halls.hall_id", index=True, max_length=36)
    
    # Relationships
    created_by_hall_admin: Optional["HallAdmin"] = Relationship(back_populates="student_accounts_created")
    student_hall: Optional["StudentHall"] = Relationship(back_populates="hall_resident_students")
    student_feedbacks: List["Feedback"] = Relationship(back_populates="student")
    student_dinning_data: List["DinningData"] = Relationship(back_populates="student")