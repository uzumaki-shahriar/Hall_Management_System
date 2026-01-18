from sqlmodel import Session, select
from typing import Optional
from ..models.student_hall_model import StudentHall

def get_all_student_halls(db: Session) -> list[StudentHall]:
    statement = select(StudentHall)
    results = db.exec(statement).all()
    return results

def get_student_hall_by_id(db: Session, hall_id: int) -> Optional[StudentHall]:
    statement = select(StudentHall).where(StudentHall.hall_id == hall_id)
    result = db.exec(statement).first()
    return result

def create_student_hall(db: Session, student_hall: StudentHall) -> StudentHall:
    db.add(student_hall)
    db.commit()
    db.refresh(student_hall)
    return student_hall

def get_student_halls_by_university(db: Session, university_name: str) -> list[StudentHall]:
    statement = select(StudentHall).where(StudentHall.associated_university_name == university_name)
    results = db.exec(statement).all()
    return results

def get_student_hall_name_by_hall_id(db: Session, hall_id: int) -> Optional[str]:
    statement = select(StudentHall.hall_name).where(StudentHall.hall_id == hall_id)
    result = db.exec(statement).first()
    return result