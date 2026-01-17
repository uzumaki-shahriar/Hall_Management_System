from sqlmodel import Session
from fastapi import Depends, HTTPException, status
from ..models.super_admin_model import SuperAdmin
from ..schemas.super_admin_schema import SuperAdminLoginRequest, SuperAdminProfileResponse, SuperAdminSignUpRequest
from ..schemas.helper_schema import TokenResponse, MessageResponse
from ..crud import super_admin_crud as spdmin
from ..utils.security import hash_password, verify_password,create_access_token, get_token_expiration_seconds


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
    
    

