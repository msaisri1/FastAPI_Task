from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, users
# from app.core.config import settings
from app.db.base import init_db
from fastapi.openapi.utils import get_openapi

PROJECT_NAME : str = "User Management Service"
API_PREFIX : str = "/api"

# Initialize the database tables
init_db()

# Create FastAPI instance
app = FastAPI(
    title=PROJECT_NAME,
    # openapi_url=f"{API_PREFIX}/openapi.json"
)

# Custom OpenAPI schema with Bearer auth
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=PROJECT_NAME,
        version="1.0.0",
        description="API for managing users with JWT Auth",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for operation in path.values():
            operation["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

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