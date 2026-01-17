from sqlmodel import Session, select
from typing import Optional
from ..models.super_admin_model import SuperAdmin

def get_super_admin_by_email(db: Session, email: str) -> Optional[SuperAdmin]:
    statement = select(SuperAdmin).where(SuperAdmin.super_admin_email == email)
    result = db.exec(statement).first()
    return result

def get_super_admin_by_id(db: Session, super_admin_id: int) -> Optional[SuperAdmin]:
    statement = select(SuperAdmin).where(SuperAdmin.super_admin_id == super_admin_id)
    result = db.exec(statement).first()
    return result


def create_super_admin(db: Session, super_admin: SuperAdmin) -> SuperAdmin:
    db.add(super_admin)
    db.commit()
    db.refresh(super_admin)
    return super_admin

