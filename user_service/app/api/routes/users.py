from fastapi import APIRouter, HTTPException, Depends, status
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

# DELETE specific user by email
@router.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(role_required("admin"))):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": f"User with ID {user_id} deleted."}


# DELETE all users (admin only)
@router.delete("/users", status_code=status.HTTP_204_NO_CONTENT)
def delete_all_users(db: Session = Depends(get_db), current_user=Depends(role_required("admin"))):
    users = db.query(User).all()
    if not users:
        return {"message": "No users found to delete."}
    
    for user in users:
        db.delete(user)
    db.commit()
    return {"message": "All users have been deleted."}