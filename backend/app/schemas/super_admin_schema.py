from pydantic import BaseModel, EmailStr

class SuperAdminSignUpRequest(BaseModel):

    super_admin_name: str
    super_admin_email: EmailStr
    super_admin_password: str
    super_admin_confirm_password: str

class SuperAdminLoginRequest(BaseModel):
    super_admin_email: EmailStr
    super_admin_password: str

class SuperAdminProfileResponse(BaseModel):
    super_admin_id: str
    super_admin_email: EmailStr
    super_admin_name: str

    class Config:
        from_attributes = True

