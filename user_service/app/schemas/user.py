from pydantic import BaseModel, EmailStr
from typing import Optional

# Common base for user info
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

# Used during registration
class UserCreate(UserBase):
    password: str
    role: str = "user"

# Used for updating profile info
class UserUpdate(BaseModel):
    full_name: Optional[str] = None

#Internal DB representation(not returned directly)
class UserInDB(UserBase):
    id: int
    hashed_password: str
    role: str

    class Config:
        from_attributes = True

# Returned to Clinet
class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: str

    class Config:
        from_attributes = True

# JWT token schema
class Token(BaseModel):
    access_token: str
    token_type: str