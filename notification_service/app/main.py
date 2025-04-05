import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.consumer import start_consumer

@asynccontextmanager
async def lifespan(app: FastAPI):
    connection = await start_consumer()
    yield
    await connection.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "Notification service is running.."}