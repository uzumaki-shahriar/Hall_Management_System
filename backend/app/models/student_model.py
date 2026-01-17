from typing import Optional, TYPE_CHECKING, List
from sqlmodel import Field, SQLModel, Relationship
from decimal import Decimal



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
    student_room_number: Optional[int] = Field(default=None, max_length=10, nullable=True)
    student_hashed_password: str = Field(max_length=255)

    # Relationships