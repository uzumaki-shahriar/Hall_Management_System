from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import date
import uuid

if TYPE_CHECKING:
    from ..models.student_model import Student

class Feedback(SQLModel, table=True):

    __tablename__ = "feedbacks"
    feedback_id: str = Field(primary_key=True, index=True, default_factory=lambda: str(uuid.uuid4()), max_length=36)
    feedback_student_id: str = Field(foreign_key="students.student_id", index=True, max_length=36)
    feedback_text: str = Field(max_length=1000)
    feedback_date: Optional[date] = Field(default_factory=lambda: date.today())

    # Relationships
    student: Optional["Student"] = Relationship(back_populates="student_feedbacks")