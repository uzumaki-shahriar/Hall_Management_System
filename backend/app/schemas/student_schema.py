from pydantic import BaseModel, EmailStr, Field


class StudentSignUpRequest(BaseModel):
    
    student_id: str = Field(..., max_length=8)
    student_email: EmailStr
    student_name: str = Field(..., max_length=100)
    student_room_number: int = Field(..., max_length=10)
    student_batch: str = Field(..., max_length=10)
    student_department: str = Field(..., max_length=50)

class StudentLoginRequest(BaseModel):
    
    student_id: str = Field(..., max_length=8)
    student_email: EmailStr
    student_password: str = Field(..., min_length=8, max_length=100)

class StudentProfileResponse(BaseModel):

    student_id: str
    student_email: EmailStr
    student_name: str
    student_department: str
    student_batch: str
    student_room_number: int
    student_contact_number: str
    student_home_address: str
    student_hall_name: str

    class Config:
        from_attributes = True

class StudentProfileUpdateRequest(BaseModel):

    student_contact_number: str = Field(..., max_length=15)
    student_home_address: str = Field(..., max_length=200)



