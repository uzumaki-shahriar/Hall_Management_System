from fastapi import HTTPException, APIRouter, status, Depends
from sqlmodel import Session
from ...db.session import get_session
from ...schemas.student_schema import StudentProfileResponse, StudentLoginRequest, StudentProfileUpdateRequest, StudentPasswordChangeRequest
from ...schemas.helper_schema import TokenResponse, MessageResponse
from ...services.student_service import StudentService
from ...utils.dependencies import get_current_student
from ...models.student_model import Student

router = APIRouter(
    prefix="/student",
    tags=["Student"]
)

@router.post("/login",
             response_model=TokenResponse,
                status_code=status.HTTP_200_OK,
                summary="Student Login",
                description="Endpoint for student to log in.")
async def student_login(
    login_data: StudentLoginRequest,
    db: Session = Depends(get_session)
):
    token_response = StudentService.login_student(
        db,
        login_data
    )
    return token_response

@router.get("/profile",
            response_model=StudentProfileResponse,
            status_code=status.HTTP_200_OK,
            summary="Get Student Profile",
            description="Endpoint to get student profile details.")
async def get_student_profile(
    db: Session = Depends(get_session),
    student: Student = Depends(get_current_student)
):
    student_profile = StudentService.get_student_profile(
        db,
        student.student_id
    )
    return student_profile


@router.put("/update_profile",
            response_model=MessageResponse,
            status_code=status.HTTP_200_OK,
            summary="Update Student Profile",
            description="Endpoint to update student profile details.")
async def update_student_profile(
    update_data: StudentProfileUpdateRequest,
    db: Session = Depends(get_session),
    student: Student = Depends(get_current_student)
):
    message_response = StudentService.update_student_information(
        db,
        student.student_id,
        update_data
    )
    return message_response


@router.put("/change_password",
            response_model=MessageResponse,
            status_code=status.HTTP_200_OK,
            summary="Change Student Password",
            description="Endpoint to change student account password.")
async def change_student_password(
    change_password_data: StudentPasswordChangeRequest,
    db: Session = Depends(get_session),
    student: Student = Depends(get_current_student)
) -> MessageResponse:
    message_response = StudentService.change_student_password(
        db,
        student.student_email,
        change_password_data
    )
    return message_response
