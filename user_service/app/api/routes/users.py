from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.user import UserOut
from app.services.user_service import get_current_user
from app.core.security import get_current_user
from app.core.rbac import role_required
from app.db.models.user import User

router = APIRouter()

@router.get("/user/me", response_model=UserOut)
def read_my_profile(
    current_user: User = Depends(get_current_user),
):
    return current_user

@router.get("/users", response_model=List[UserOut], dependencies=[Depends(role_required("admin"))])
def list_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()