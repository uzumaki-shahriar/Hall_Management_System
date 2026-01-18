from sqlmodel import Session
from fastapi import Depends, HTTPException, status
from ..models.super_admin_model import SuperAdmin
from ..models.student_hall_model import StudentHall
from ..models.hall_admin_model import HallAdmin
from ..schemas.super_admin_schema import SuperAdminLoginRequest, SuperAdminProfileResponse, SuperAdminSignUpRequest
from ..schemas.helper_schema import TokenResponse, MessageResponse
from ..schemas.student_hall_schema import StudentHallCreationRequest
from ..schemas.hall_admin_schema import HallAdminSignUpRequest
from ..crud import super_admin_crud as spdmin, hall_admin_crud as hadmin, student_hall_crud as sthall
from ..utils.security import hash_password, verify_password,create_access_token, get_token_expiration_seconds
from ..utils.passwordGenerator import generate_hall_admin_password
from ..utils.emailsender import send_hall_admin_credentials

class SuperAdminService:

    @staticmethod
    def sign_up_super_admin(
        db: Session,
        super_admin_data: SuperAdminSignUpRequest
    )-> SuperAdmin:
        if super_admin_data.super_admin_password != super_admin_data.super_admin_confirm_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Passwords do not match"
            )
        existing_admin = spdmin.get_super_admin_by_email(
            db, super_admin_data.super_admin_email
        )
        if existing_admin:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Super Admin with this email already exists"
            )
        hashed_password = hash_password(super_admin_data.super_admin_password)
        new_super_admin = SuperAdmin(
            
            super_admin_email=super_admin_data.super_admin_email,
            super_admin_name=super_admin_data.super_admin_name,
            super_admin_hashed_password=hashed_password
        )
        return spdmin.create_super_admin(db, new_super_admin)
        
    
    @staticmethod
    def login_super_admin(
        db: Session,
        login_data: SuperAdminLoginRequest
    ) -> TokenResponse:
        super_admin = spdmin.get_super_admin_by_email(
            db, login_data.super_admin_email
        )
        if not super_admin:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Super Admin with this email not found"
            )
        if not verify_password(
            login_data.super_admin_password,
            super_admin.super_admin_hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password"
            )
        access_token = create_access_token(
            data={"sub": super_admin.super_admin_id,
                  "role": "super_admin"}
        )
        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            expires_in=get_token_expiration_seconds()
        )
    
    @staticmethod
    def get_super_admin_profile(
        db: Session,
        current_super_admin: SuperAdmin
    )-> SuperAdminProfileResponse:
        super_admin = spdmin.get_super_admin_by_email(
            db, current_super_admin.super_admin_email
        )
        if not super_admin:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Super Admin with this email not found"
            )
        return SuperAdminProfileResponse(
            super_admin_id=super_admin.super_admin_id,
            super_admin_email=super_admin.super_admin_email,
            super_admin_name=super_admin.super_admin_name
        )
    
    @staticmethod
    def create_student_hall(
        db: Session,
        student_hall_data: StudentHallCreationRequest,
        hall_admin_data: HallAdminSignUpRequest,
        creator_super_admin_id: str
    ):
        new_student_hall = sthall.create_student_hall(
            db,
            StudentHall(
                hall_name=student_hall_data.hall_name,
                asscociated_university_name=student_hall_data.associated_university_name,
                hall_dinning_fee=student_hall_data.hall_dinning_fee,
                total_rooms=student_hall_data.total_rooms,
                created_by_super_admin_id=creator_super_admin_id
            )
        )
        existing_admin = hadmin.get_hall_admin_by_email(
            db, hall_admin_data.hall_admin_email
        )        
        if existing_admin:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Hall Admin with this email already exists"
            )
        generated_password = generate_hall_admin_password()
        hashed_password = hash_password(generated_password)
        new_hall_admin = hadmin.create_hall_admin(
            db,
            HallAdmin(
                hall_admin_email=hall_admin_data.hall_admin_email,
                hall_admin_contact_number=hall_admin_data.hall_admin_contact_number,
                hall_admin_hashed_password=hashed_password,
                asscociated_hall_id=new_student_hall.hall_id
            )
        )
        send_hall_admin_credentials(
            hall_admin_email=hall_admin_data.hall_admin_email,
            hall_name=new_student_hall.hall_name,
            hall_admin_password=generated_password
        )
        
        return {
            "student_hall": new_student_hall,
            "hall_admin": new_hall_admin
        }

