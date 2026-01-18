from fastapi import HTTPException, APIRouter, status, Depends
from sqlmodel import Session
from ...db.session import get_session
from ...schemas.feedback_schema import FeedbackCreateRequest, FeedbackResponse
from ...schemas.helper_schema import MessageResponse
from ...services.feedback_service import FeedbackService
from ...utils.dependencies import get_current_student
from ...models.student_model import Student
from ...models.feedback_model import Feedback

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"]
)

@router.post("/submit",
                response_model=MessageResponse,
                status_code=status.HTTP_201_CREATED,
                summary="Submit Feedback",
                description="Endpoint for students to submit feedback.")
async def submit_feedback(
    feedback_data: FeedbackCreateRequest,
    db: Session = Depends(get_session),
    student: Student = Depends(get_current_student)
) -> MessageResponse:
    message_response = FeedbackService.create_feedback(
        db,
        feedback_data,
        student.student_id
    )
    return message_response

@router.get("/all",
            response_model=list[FeedbackResponse],
            status_code=status.HTTP_200_OK,
            summary="Get All Feedbacks",
            description="Endpoint to retrieve all feedbacks submitted by students.")
async def get_all_feedbacks(
    db: Session = Depends(get_session)
) -> list[FeedbackResponse]:
    feedbacks = FeedbackService.get_all_feedbacks(db)
    return feedbacks

@router.get("/student/feedbacks",
            response_model=list[FeedbackResponse],
            status_code=status.HTTP_200_OK,
            summary="Get Student Feedbacks",
            description="Endpoint to retrieve feedbacks submitted by the current student."
)
async def get_student_feedbacks(
    db: Session = Depends(get_session),
    student: Student = Depends(get_current_student)
) -> list[FeedbackResponse]:
    feedbacks = FeedbackService.get_all_feedback_of_a_student(db, student.student_id)
    return feedbacks
    