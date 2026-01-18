from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class FeedbackCreateRequest(BaseModel):

    feedback_text: str = Field(..., max_length=1000)
    feedback_date: Optional[date] = Field(default_factory=lambda: date.today())

class FeedbackResponse(BaseModel):

    feedback_id: str
    feedback_text: str
    feedback_date: date
    feedback_given_by: str

    class Config:
        from_attributes = True

