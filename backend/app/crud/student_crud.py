from sqlmodel import Session, select
from typing import Optional
from ..models.student_model import Student

def get_student_by_id(db: Session, student_id: str) -> Optional[Student]:
    statement = select(Student).where(Student.student_id == student_id)
    result = db.exec(statement).first()
    return result

def get_student_by_email(db: Session, student_email: str) -> Optional[Student]:
    statement = select(Student).where(Student.student_email == student_email)
    result = db.exec(statement).first()
    return result

def create_student(db: Session, student: Student) -> Student:
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def update_student(db: Session, student: Student) -> Student:
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def change_student_password(db: Session, student_email: str, new_hashed_password: str) -> None:
    student = get_student_by_email(db, student_email)
    if student:
        student.student_hashed_password = new_hashed_password
        db.add(student)
        db.commit()