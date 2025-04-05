from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, Token, UserOut, UserUpdate
from app.services.user_service import create_user, authenticate_user, get_current_user, update_user
from app.core.security import create_access_token
from app.db.session import get_db
from app.core.rbac import role_required
from app.services.publisher import publish_user_registered

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=Token)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_in)
    token = create_access_token({"sub": user.email, "role": user.role})
    publish_user_registered(user)
    return {"access_token": token, "token_type":"bearer"}

@router.post("/login", response_model=Token)
def login(user_in: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_in.email, user_in.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    token = create_access_token({"sub": user.email, "role": user.role})
    return {"access_token": token, "token_type":"bearer"}

# @router.get("/me", response_model=UserOut)
# def get_profile(current_user=Depends(get_current_user)):
#     return current_user

# @router.put("/me", response_model=UserOut)
# def update_profile(user_update: UserUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
#     return(update_user(db, current_user, user_update))

@router.get("/admin", dependencies=[Depends(role_required("admin"))])
def admin_only():
    return {"msg": "You are an admin"}