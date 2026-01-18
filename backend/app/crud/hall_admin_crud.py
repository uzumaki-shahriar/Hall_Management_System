from sqlmodel import Session, select
from typing import Optional
from ..models.hall_admin_model import HallAdmin

def get_all_hall_admins(db: Session) -> list[HallAdmin]:
    statement = select(HallAdmin)
    results = db.exec(statement).all()
    return results

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

def get_hall_id_of_hall_admin(db: Session, hall_admin_email: str) -> Optional[str]:
    statement = select(HallAdmin.asscociated_hall_id).where(HallAdmin.hall_admin_email == hall_admin_email)
    result = db.exec(statement).first()
    return result

def update_hall_admin_password(db: Session, hall_admin_email: str, new_hashed_password: str) -> None:
    hall_admin = get_hall_admin_by_email(db, hall_admin_email)
    if hall_admin:
        hall_admin.hall_admin_hashed_password = new_hashed_password
        db.add(hall_admin)
        db.commit()
        