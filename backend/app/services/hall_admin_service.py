from sqlmodel import Session
from fastapi import Depends, HTTPException, status
from ..models.hall_admin_model import HallAdmin
from ..models.student_hall_model import StudentHall
from ..schemas.hall_admin_schema import HallAdminLoginRequest, HallAdminProfileResponse, HallAdminChangePasswordRequest
from ..schemas.helper_schema import TokenResponse
from ..crud import hall_admin_crud as hadmin
from ..crud import student_hall_crud as sthall
from ..utils.security import verify_password, create_access_token, get_token_expiration_seconds, hash_password

class HallAdminService:

    @staticmethod
    def login_hall_admin(
        db: Session,
        login_data: HallAdminLoginRequest
    )-> TokenResponse:
        hall_admin = hadmin.get_hall_admin_by_email(
            db, login_data.hall_admin_email
        )
        if not hall_admin:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hall Admin with this email not found"
            )
        asscociated_hall_id = hall_admin.asscociated_hall_id
        asscociated_hall_name = sthall.get_student_hall_name_by_hall_id(
            db, asscociated_hall_id
        )
        if login_data.asscociated_hall_name != asscociated_hall_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This Hall Admin is not associated with the provided hall name"
            )
        if not verify_password(
            login_data.hall_admin_password,
            hall_admin.hall_admin_hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password"
            )
        access_token_expires = get_token_expiration_seconds()
        access_token = create_access_token(
            data={"sub": hall_admin.hall_admin_email,
                  "role": "hall_admin"}
        )
        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            expires_in=access_token_expires
        )
    
    @staticmethod
    def get_hall_admin_profile(
        db: Session,
        hall_admin_id: str
    )-> HallAdminProfileResponse:
        hall_admin = hadmin.get_hall_admin_by_id(
            db, hall_admin_id
        )
        if not hall_admin:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hall Admin with this ID not found"
            )
        return HallAdminProfileResponse(
            hall_admin_id=hall_admin.hall_admin_id,
            hall_admin_email=hall_admin.hall_admin_email,
            hall_admin_contact_number=hall_admin.hall_admin_contact_number
        )
    
    @staticmethod
    def get_all_hall_admins(
        db: Session
    )-> list[HallAdminProfileResponse]:
        hall_admins = hadmin.get_all_hall_admins(db)
        hall_admins_profiles = []
        for hall_admin in hall_admins:
            hall_admins_profiles.append(
                HallAdminProfileResponse(
                    hall_admin_id=hall_admin.hall_admin_id,
                    hall_admin_email=hall_admin.hall_admin_email,
                    hall_admin_contact_number=hall_admin.hall_admin_contact_number
                )
            )
        return hall_admins_profiles
    
    @staticmethod
    def change_hall_admin_password(
        db: Session,
        hall_admin_email: str,
        changed_password_data: HallAdminChangePasswordRequest
    ) -> None:
        hall_admin = hadmin.get_hall_admin_by_email(
            db, hall_admin_email
        )
        if not hall_admin:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hall Admin with this email not found"
            )
        if not verify_password(
            changed_password_data.old_password,
            hall_admin.hall_admin_hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Current password is incorrect"
            )
        if changed_password_data.new_password != changed_password_data.confirm_new_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="New password and confirm new password do not match"
            )
        new_hashed_password = hash_password(
            changed_password_data.new_password
        )
        hadmin.update_hall_admin_password(
            db,
            hall_admin_email,
            new_hashed_password
        )