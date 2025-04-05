# import os
# from pydantic import

# class Settings(BaseSettings):
#     # App
#     PROJECT_NAME : str = "User Management Service"
#     API_PREFIX : str = "/api"

#     # Database
#     DATABASE_URL : str = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:password@localhost:5432/user_db")

#     # JWT
#     SECRET_KEY : str = os.getenv("SECRET_KEY", "your-secret-key")
#     ALGORITHM : str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 1 #1min

#     class Config:
#         case_sensitive = True

# settings = Settings()