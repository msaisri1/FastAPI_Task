from app.db.models import user
from app.db.session import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def init_db():
    import app.db.models.user
    Base.metadata.create_all(bind=engine)