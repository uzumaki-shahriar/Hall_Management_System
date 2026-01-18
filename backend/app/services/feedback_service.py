from sqlmodel import Session
from fastapi import Depends, HTTPException, status
from typing import List
from ..models.feedback_model import Feedback
from ..models.student_model import Student
from ..crud import feedback_crud as fcrud
from ..crud import student_crud as scrud
from ..schemas.feedback_schema import FeedbackCreateRequest, FeedbackResponse
from ..schemas.helper_schema import MessageResponse

class FeedbackService:

    @staticmethod
    def create_feedback(
        db: Session,
        feedback_data: FeedbackCreateRequest,
        student_id: int
    ) -> MessageResponse:
        student: Student = scrud.get_student_by_id(db, student_id)
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )
        feedback=fcrud.create_feedback(
            db,
            Feedback(
                feedback_student_id=student_id,
                feedback_text=feedback_data.feedback_text,
                feedback_date=feedback_data.feedback_date
            )
        )
        return MessageResponse(
            response_code=status.HTTP_201_CREATED,
            message="Feedback created successfully",
            success=True
        )
    

    @staticmethod
    def get_all_feedbacks(
        db: Session
    ) -> List[FeedbackResponse]:
        feedbacks: List[Feedback] = fcrud.get_all_feedbacks(db)
        return [
            FeedbackResponse(
                feedback_id=feedback.feedback_id,
                feedback_text=feedback.feedback_text,
                feedback_date=feedback.feedback_date,
                feedback_given_by=scrud.get_student_by_id(db, feedback.feedback_student_id).student_name
            )
            for feedback in feedbacks
        ]
    
    @staticmethod
    def get_all_feedback_of_a_student(
        db: Session,
        student_id: int
    ) -> List[FeedbackResponse]:
        student: Student = scrud.get_student_by_id(db, student_id)
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )
        feedbacks: List[Feedback] = fcrud.get_all_feedback_of_a_student(db, student_id)
        return [
            FeedbackResponse(
                feedback_id=feedback.feedback_id,
                feedback_text=feedback.feedback_text,
                feedback_date=feedback.feedback_date,
                feedback_given_by=student.student_name
            )
            for feedback in feedbacks
        ]
    