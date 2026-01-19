from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import date
import uuid

if TYPE_CHECKING:
    from ..models.student_model import Student

class DinningData(SQLModel, table=True):

    __tablename__ = "dinning_data"
    dinning_data_id: str = Field(primary_key=True, index=True, default_factory=lambda: str(uuid.uuid4()), max_length=36)
    dinning_student_id: str = Field(foreign_key="students.student_id", index=True, max_length=36)
    dinning_item_name: str = Field(max_length=100)
    dinning_item_quantity: int = Field()
    dinning_item_total_price: float = Field()
    dinning_date: Optional[date] = Field(default_factory=lambda: date.today())

    # Relationships
    student: Optional["Student"] = Relationship(back_populates="student_dinning_data")