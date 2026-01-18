from fastapi import HTTPException, APIRouter, status, Depends
from sqlmodel import Session
from ...db.session import get_session
from ...schemas.hall_admin_schema import HallAdminLoginRequest, HallAdminProfileResponse, HallAdminChangePasswordRequest
from ...schemas.helper_schema import TokenResponse, MessageResponse
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
):
    message_response = HallAdminService.change_hall_admin_password(
        db,
        hall_admin.hall_admin_email,
        change_password_data
    )
    return message_response