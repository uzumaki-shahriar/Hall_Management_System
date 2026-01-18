from fastapi import APIRouter

from ..routes import super_admin_api, hall_admin_api, student_hall_api, student_api, feedback_api

api_router = APIRouter(
    prefix="/api/v1",
    tags=["API Root"] 
)

api_router.include_router(super_admin_api.router)
api_router.include_router(hall_admin_api.router)
api_router.include_router(student_hall_api.router)
api_router.include_router(student_api.router)
api_router.include_router(feedback_api.router)

__all__ = ["api_router"]