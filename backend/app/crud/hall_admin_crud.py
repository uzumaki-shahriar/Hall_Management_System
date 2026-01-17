from sqlmodel import Session, select
from typing import Optional
from ..models.hall_admin_model import HallAdmin

def get_hall_admin_by_email(db: Session, email: str) -> Optional[HallAdmin]:
    statement = select(HallAdmin).where(HallAdmin.hall_admin_email == email)
    result = db.exec(statement).first()
    return result

def get_hall_admin_by_id(db: Session, hall_admin_id: int) -> Optional[HallAdmin]:
    statement = select(HallAdmin).where(HallAdmin.hall_admin_id == hall_admin_id)
    result = db.exec(statement).first()
    return result

def create_hall_admin(db: Session, hall_admin: HallAdmin) -> HallAdmin:
    db.add(hall_admin)
    db.commit()
    db.refresh(hall_admin)
    return hall_admin

def delete_hall_admin(db: Session, hall_admin: HallAdmin) -> None:
    db.delete(hall_admin)
    db.commit()

