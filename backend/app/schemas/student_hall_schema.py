from pydantic import BaseModel
from typing import Optional

class StudentHallCreationRequest(BaseModel):
    hall_name: str
    associated_university_name: str
    hall_dinning_fee: float
    total_rooms: int

class StudentHallProfileResponse(BaseModel):
    hall_id: str
    hall_name: str
    associated_university_name: str
    total_rooms: int

    class Config:
        from_attributes = True