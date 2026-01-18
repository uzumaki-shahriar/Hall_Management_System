from sqlmodel import Session, select
from typing import Optional
from ..models.student_model import Student

def get_student_by_id(db: Session, student_id: str) -> Optional[Student]:
    statement = select(Student).where(Student.student_id == student_id)
    result = db.exec(statement).first()
    return result

def get_student_by_email(db: Session, student_email: str) -> Optional[Student]:
    statement = select(Student).where(Student.email == student_email)
    result = db.exec(statement).first()
    return result

def create_student(db: Session, student: Student) -> Student:
    db.add(student)
    db.commit()
    db.refresh(student)
    return student