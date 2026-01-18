from pydantic import BaseModel, EmailStr

class HallAdminSignUpRequest(BaseModel):

    hall_admin_email: EmailStr
    hall_admin_contact_number: str

class HallAdminLoginRequest(BaseModel):
    hall_admin_email: EmailStr
    asscociated_hall_name: str
    hall_admin_password: str

class HallAdminChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str
    confirm_new_password: str

class HallAdminProfileResponse(BaseModel):
    hall_admin_id: str
    hall_admin_email: EmailStr
    hall_admin_contact_number: str

    class Config:
        from_attributes = True