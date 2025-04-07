from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, Token
from app.services.user_service import create_user, authenticate_user
from app.core.security import create_access_token
from app.db.session import get_db
from app.core.rbac import role_required
from app.services.publisher import publish_user_registered
from loguru import logger

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

@router.get("/admin", dependencies=[Depends(role_required("admin"))])
def admin_only():
    return {"msg": "You are an admin"}