from sqlmodel import Session, select
from typing import Optional
from ..models.feedback_model import Feedback

def get_all_feedbacks(db: Session) -> list[Feedback]:
    statement = select(Feedback)
    results = db.exec(statement).all()
    return results

def get_all_feedback_of_a_student(db: Session, student_id: int) -> list[Feedback]:
    statement = select(Feedback).where(Feedback.feedback_student_id == student_id)
    results = db.exec(statement).all()
    return results

def create_feedback(
    db: Session,
    feedback: Feedback
) -> Feedback:
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback