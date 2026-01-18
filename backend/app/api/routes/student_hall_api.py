from fastapi import HTTPException, APIRouter, status, Depends
from sqlmodel import Session
from ...db.session import get_session
from ...schemas.student_hall_schema import StudentHallProfileResponse
from ...schemas.helper_schema import MessageResponse
from ...services.hall_admin_service import HallAdminService


router = APIRouter(
    prefix="/student_hall",
    tags=["Student Hall"]
)

@router.get("/all_student_halls",
            response_model=list[StudentHallProfileResponse],
            status_code=status.HTTP_200_OK,
            summary="Get All Student Halls",
            description="Endpoint to get all student halls.")
async def get_all_student_halls(
    db: Session = Depends(get_session)
):
    student_halls_profiles = HallAdminService.get_all_student_halls(db)
    return student_halls_profiles