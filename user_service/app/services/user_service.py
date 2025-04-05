from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate
from app.db.models.user import User
from app.core.security import get_password_hash, verify_password

def create_user(db: Session, user_in: UserCreate):
    hashed_password = get_password_hash(user_in.password)
    db_user = User(email=user_in.email, full_name=user_in.full_name, hashed_password=hashed_password, role=user_in.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email==email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def update_user(db:Session, user: User, updates: UserUpdate):
    if updates.full_name:
        user.full_name = updates.full_name
    db.commit()
    db.refresh(user)
    return user

def get_current_user(db: Session, email:str):
    return db.query(User).filter(User.email == email).first()