from fastapi import HTTPException, APIRouter, status, Depends
from sqlmodel import Session
from ...db.session import get_session
from ...schemas.super_admin_schema import SuperAdminSignUpRequest, SuperAdminLoginRequest, SuperAdminProfileResponse
from ...schemas.helper_schema import TokenResponse, MessageResponse
from ...schemas.student_hall_schema import StudentHallCreationRequest
from ...schemas.hall_admin_schema import HallAdminSignUpRequest
from ...services.super_admin_service import SuperAdminService
from ...utils.dependencies import get_current_super_admin
from ...models.super_admin_model import SuperAdmin

router = APIRouter(
    prefix="/super_admin",
    tags=["Super Admin"]
)

@router.post("/signup", 
             response_model=MessageResponse,
             status_code=status.HTTP_201_CREATED,
             summary="Super Admin Sign Up",
             description="Endpoint for super admin to sign up.")
async def super_admin_sign_up(
    sign_up_data: SuperAdminSignUpRequest,
    db: Session = Depends(get_session)
):
    new_super_admin = SuperAdminService.sign_up_super_admin(
        db,
        sign_up_data
    )
    return MessageResponse(
        response_code=status.HTTP_201_CREATED,
        message=f"Super Admin {new_super_admin.super_admin_name} registered successfully",
        success=True
    )

@router.post("/login",
             response_model=TokenResponse,
                status_code=status.HTTP_200_OK,
                summary="Super Admin Login",
                description="Endpoint for super admin to log in.")
async def super_admin_login(
    login_data: SuperAdminLoginRequest,
    db: Session = Depends(get_session)
):
    token_response = SuperAdminService.login_super_admin(
        db,
        login_data
    )
    return token_response

@router.get("/profile",
            response_model=SuperAdminProfileResponse,
            status_code=status.HTTP_200_OK,
            summary="Get Super Admin Profile",
            description="Endpoint to get super admin profile details.")

async def get_super_admin_profile(
    db: Session = Depends(get_session),
    super_admin: SuperAdmin = Depends(get_current_super_admin)
):
    return SuperAdminService.get_super_admin_profile(db, super_admin)


@router.post("/create_student_hall",
             response_model=MessageResponse,
             status_code=status.HTTP_201_CREATED,
             summary="Create Student Hall with Hall Admin",
             description="Endpoint for super admin to create a student hall along with registering a hall admin.")
async def create_student_hall_with_hall_admin(
    student_hall_data: StudentHallCreationRequest,
    hall_admin_data: HallAdminSignUpRequest,
    db: Session = Depends(get_session),
    super_admin: SuperAdmin = Depends(get_current_super_admin)
):
    result = SuperAdminService.create_student_hall(
        db,
        student_hall_data,
        hall_admin_data,
        super_admin.super_admin_id
    )
    return MessageResponse(
        response_code=status.HTTP_201_CREATED,
        message="Student Hall created successfully with Hall Admin",
        success=True
    )

