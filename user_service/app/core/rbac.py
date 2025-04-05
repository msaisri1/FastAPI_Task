from fastapi import Depends, HTTPException
from app.core.security import get_current_user

def role_required(role: str):
    def role_dependency(current_user=Depends(get_current_user)):
        if current_user.role != role:
            raise HTTPException(status_code=403, detail="Access forbidden: Insufficient role")
    return role_dependency