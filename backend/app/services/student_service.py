from sqlmodel import Session
from fastapi import Depends, HTTPException, status
from ..models.student_model import Student
from ..schemas.student_schema import StudentLoginRequest, StudentProfileResponse, StudentProfileUpdateRequest, StudentPasswordChangeRequest
from ..schemas.helper_schema import TokenResponse, MessageResponse
from ..crud import student_crud as student_crud, student_hall_crud
from ..utils.security import hash_password, verify_password, create_access_token, get_token_expiration_seconds


class StudentService:

    @staticmethod
    def login_student(
        db: Session,
        login_data: StudentLoginRequest
    ) -> TokenResponse:
        student = student_crud.get_student_by_email(
            db, login_data.student_email
        )
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student with this email not found"
            )
        if not verify_password(
            login_data.student_password,
            student.student_hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password"
            )
        access_token = create_access_token(
            data={"sub": student.student_id,
                  "role": "student"}
        )
        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            expires_in=get_token_expiration_seconds(access_token)
        )
    
    @staticmethod
    def get_student_profile(
        db: Session,
        student_id: str
    ) -> StudentProfileResponse:
        student = student_crud.get_student_by_id(
            db, student_id
        )
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )
        student_hall_name = student_hall_crud.get_student_hall_name_by_hall_id(
            db, student.student_hall_id
        )
        return StudentProfileResponse(
            student_id=student.student_id,
            student_email=student.student_email,
            student_name=student.student_name,
            student_department=student.student_department,
            student_batch=student.student_batch,
            student_room_number=student.student_room_number,
            student_contact_number=student.student_contact_number,
            student_home_address=student.student_home_address,
            student_hall_name=student_hall_name
        )
        

    @staticmethod
    def update_student_information(
        db: Session,
        student_id: str,
        update_data: StudentProfileUpdateRequest
    ) -> MessageResponse:
        
        student = student_crud.get_student_by_id(
            db, student_id
        )
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )
        student.student_contact_number = update_data.student_contact_number
        student.student_home_address = update_data.student_home_address
        student_crud.update_student(db, student)
        return MessageResponse(
            response_code=status.HTTP_200_OK,
            message="Student information updated successfully",
            success=True
        )
    

    @staticmethod
    def change_student_password(
        db: Session,
        student_email: str,
        password_data: StudentPasswordChangeRequest
    )-> MessageResponse:
        student = student_crud.get_student_by_email(
            db, student_email
        )
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student with this email not found"
            )
        if not verify_password(
            password_data.current_password,
            student.student_hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Current password is incorrect"
            )
        if password_data.new_password != password_data.confirm_new_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="New password and confirm password do not match"
            )
        new_hashed_password = hash_password(
            password_data.new_password
        )
        student_crud.change_student_password(
            db, student_email, new_hashed_password
        )
        return MessageResponse(
            response_code=status.HTTP_200_OK,
            message="Password changed successfully",
            success=True
        )