from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, users
# from app.core.config import settings
from app.db.base import init_db

PROJECT_NAME : str = "User Management Service"
API_PREFIX : str = "/api"

# Initialize the database tables
init_db()

# Create FastAPI instance
app = FastAPI(
    title=PROJECT_NAME,
    openapi_url=f"{API_PREFIX}/openapi.json"
)

# Middleware (CORS)
app.middleware(
    CORSMiddleware,
    # allow_origins=["*"],
    # allow_creadentails = True,
    # allow_methods=["*"],
    # allow_headers=["*"],
)

# Include routes
app.include_router(auth.router, prefix=API_PREFIX, tags=["auth"])
app.include_router(users.router, prefix=API_PREFIX, tags=["users"])

# Health check route
@app.get("/ping")
def ping():
    return{"message": "pong"}