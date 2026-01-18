from fastapi import HTTPException, APIRouter, status, Depends
from sqlmodel import Session
from ...db.session import get_session
from ...schemas.hall_admin_schema import HallAdminLoginRequest, HallAdminProfileResponse, HallAdminChangePasswordRequest
from ...schemas.helper_schema import TokenResponse, MessageResponse
from ...schemas.student_hall_schema import StudentHallProfileResponse
from ...schemas.student_schema import StudentSignUpRequest, StudentProfileResponse
from ...services.hall_admin_service import HallAdminService
from ...utils.dependencies import get_current_hall_admin
from ...models.hall_admin_model import HallAdmin

router = APIRouter(
    prefix="/hall_admin",
    tags=["Hall Admin"]
)
@router.post("/login",
             response_model=TokenResponse,
                status_code=status.HTTP_200_OK,
                summary="Hall Admin Login",
                description="Endpoint for hall admin to log in.")
async def hall_admin_login(
    login_data: HallAdminLoginRequest,
    db: Session = Depends(get_session)
):
    token_response = HallAdminService.login_hall_admin(
        db,
        login_data
    )
    return token_response

@router.get("/profile",
            response_model=HallAdminProfileResponse,
            status_code=status.HTTP_200_OK,
            summary="Get Hall Admin Profile",
            description="Endpoint to get hall admin profile details.")
async def get_hall_admin_profile(
    db: Session = Depends(get_session),
    hall_admin: HallAdmin = Depends(get_current_hall_admin)
):
    hall_admin_profile = HallAdminService.get_hall_admin_profile(
        db,
        hall_admin.hall_admin_id
    )
    return hall_admin_profile


@router.get("/all",
            response_model=list[HallAdminProfileResponse],
            status_code=status.HTTP_200_OK,
            summary="Get All Hall Admins",
            description="Endpoint to get all hall admins.")
async def get_all_hall_admins(
    db: Session = Depends(get_session)
):
    hall_admins_profiles = HallAdminService.get_all_hall_admins(db)
    return hall_admins_profiles

@router.put("/change_password",
            response_model=MessageResponse,
            status_code=status.HTTP_200_OK,
            summary="Change Hall Admin Password",
            description="Endpoint for hall admin to change their password.")
async def change_hall_admin_password(
    change_password_data: HallAdminChangePasswordRequest,
    db: Session = Depends(get_session),
    hall_admin: HallAdmin = Depends(get_current_hall_admin)
)-> MessageResponse:
    message_response = HallAdminService.change_hall_admin_password(
        db,
        hall_admin.hall_admin_email,
        change_password_data
    )
    return message_response

@router.get("/profile/student_hall",
            response_model=StudentHallProfileResponse,
            status_code=status.HTTP_200_OK,
            summary="Get Associated Student Hall Profile",
            description="Endpoint to get the profile of the student hall associated with the hall admin.")
async def get_associated_student_hall_profile(
    db: Session = Depends(get_session),
    hall_admin: HallAdmin = Depends(get_current_hall_admin)
):
    student_hall_profile = HallAdminService.get_hall_profile_of_admin(
        db,
        hall_admin.hall_admin_email
    )
    return student_hall_profile

@router.post("/create_student",
            response_model=MessageResponse,
            status_code=status.HTTP_201_CREATED,
            summary="Create Student Account",
            description="Endpoint for hall admin to create a student account.")
async def create_student_account(
    student_data: StudentSignUpRequest,
    db: Session = Depends(get_session),
    hall_admin: HallAdmin = Depends(get_current_hall_admin)
):
    message_response = HallAdminService.create_hall_resident_student_account(
        db,
        student_data,
        hall_admin.hall_admin_email
    )
    return message_response

@router.get("/students_in_hall",
            response_model=list[StudentProfileResponse],
            status_code=status.HTTP_200_OK,
            summary="Get All Students in Hall",
            description="Endpoint to get all students in the hall associated with the hall admin.")
async def get_all_students_in_hall(
    db: Session = Depends(get_session),
    hall_admin: HallAdmin = Depends(get_current_hall_admin)
):
    students_profiles = HallAdminService.get_all_students_in_hall(
        db,
        hall_admin.hall_admin_email
    )
    return students_profiles

@router.get("/total_students",
            response_model=int,
            status_code=status.HTTP_200_OK,
            summary="Get Total Students in Hall",
            description="Endpoint to get the total number of students in the hall associated with the hall admin")
async def get_total_students_in_hall(
    db: Session = Depends(get_session),
    hall_admin: HallAdmin = Depends(get_current_hall_admin)
):
    total_students = HallAdminService.get_total_students_in_hall(
        db,
        hall_admin.hall_admin_email
    )
    return total_students