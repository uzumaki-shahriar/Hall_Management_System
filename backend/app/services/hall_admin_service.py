from sqlmodel import Session
from fastapi import Depends, HTTPException, status
from typing import List
from ..models.hall_admin_model import HallAdmin
from ..models.student_hall_model import StudentHall
from ..models.student_model import Student
from ..schemas.hall_admin_schema import HallAdminLoginRequest, HallAdminProfileResponse, HallAdminChangePasswordRequest
from ..schemas.student_hall_schema import StudentHallProfileResponse
from ..schemas.student_schema import StudentSignUpRequest, StudentProfileResponse
from ..schemas.helper_schema import TokenResponse
from ..crud import hall_admin_crud as hadmin
from ..crud import student_hall_crud as sthall
from ..crud import student_crud as scrud    
from ..utils.security import verify_password, create_access_token, get_token_expiration_seconds, hash_password
from ..utils.passwordGenerator import generate_student_password
from ..utils.emailsender import send_student_credentials

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
        access_token = create_access_token(
            data={"sub": hall_admin.hall_admin_id,
                  "role": "hall_admin"}
        )
        access_token_expires = get_token_expiration_seconds(access_token)
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


    @staticmethod
    def get_hall_profile_of_admin(
        db: Session,
        hall_admin_email: str
    )-> StudentHallProfileResponse:
        hall_admin = hadmin.get_hall_admin_by_email(
            db, hall_admin_email
        )
        if not hall_admin:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hall Admin with this email not found"
            )
        hall_id = hall_admin.asscociated_hall_id
        student_hall = sthall.get_student_hall_by_id(
            db, hall_id
        )
        if not student_hall:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Associated Student Hall not found"
            )
        return StudentHallProfileResponse(
            hall_id=student_hall.hall_id,
            hall_name=student_hall.hall_name,
            associated_university_name=student_hall.associated_university_name,
            total_rooms=student_hall.total_rooms
        )
    
    @staticmethod
    def create_hall_resident_student_account(
        db: Session,
        student_data: StudentSignUpRequest,
        hall_admin_email: str
    )-> Student:
         hall_admin = hadmin.get_hall_admin_by_email(
            db, hall_admin_email
        )
         if not hall_admin:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hall Admin with this ID not found"
            )
         hall_id = hall_admin.asscociated_hall_id
         existing_student = scrud.get_student_by_email(
            db, student_data.email
         )
         if existing_student:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A student with this email already exists"
            )
         generated_password = generate_student_password()
         hashed_password = hash_password(generated_password)
         new_student = scrud.create_student(
             db,Student(
             student_id=student_data.student_id,
             student_email=student_data.student_email,
                student_name=student_data.student_name,
                studet_room_number=student_data.student_room_number,
                student_batch=student_data.student_batch,
                student_department=student_data.student_department,
                student_hashed_password=hashed_password,
                created_by_hall_admin_id=hall_admin.hall_admin_id,
                student_hall_id=hall_id
                )
            )
         
         send_student_credentials(
             student_email=student_data.student_email,
             student_name=student_data.student_name,
             student_password=generated_password
         )
         return new_student
    

    @staticmethod
    def get_all_students_in_hall(
        db: Session,
        hall_admin_email: str
    )-> List[StudentProfileResponse]:
        hall_admin = hadmin.get_hall_admin_by_email(
            db, hall_admin_email
        )
        if not hall_admin:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hall Admin with this email not found"
            )
        hall_id = hall_admin.asscociated_hall_id
        student_hall = sthall.get_student_hall_by_id(
            db, hall_id
        )
        if not student_hall:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Associated Student Hall not found"
            )
        students = sthall.get_all_students_in_hall(
            db, hall_id
        )
        student_profiles = []
        for student in students:
            student_profiles.append(
                StudentProfileResponse(
                    student_id=student.student_id,
                    student_email=student.student_email,
                    student_name=student.student_name,
                    student_department=student.student_department,
                    student_batch=student.student_batch,
                    student_room_number=student.student_room_number,
                    student_contact_number=student.student_contact_number,
                    student_home_address=student.student_home_address,
                    student_hall_name=student_hall.hall_name
                )
            )
        return student_profiles
        
    @staticmethod
    def get_total_students_in_hall(
        db: Session,
        hall_admin_email: str
    )-> int:
        hall_admin = hadmin.get_hall_admin_by_email(
            db, hall_admin_email
        )
        if not hall_admin:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hall Admin with this email not found"
            )
        hall_id = hall_admin.asscociated_hall_id
        student_hall = sthall.get_student_hall_by_id(
            db, hall_id
        )
        if not student_hall:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Associated Student Hall not found"
            )
        students = sthall.get_all_students_in_hall(
            db, hall_id
        )
        return len(students)
    

         

         
    


