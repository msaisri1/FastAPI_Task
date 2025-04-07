import os
import asyncio
import json
from aio_pika import connect_robust, IncomingMessage
# from app.core.config import settings
from app.services.notification_handler import send_notification

rabbitmq_url = os.getenv("RABBITMQ_HOST", "rabbitmq")

RABBITMQ_URL: str = os.getenv("RABBITMQ_URL", f"amqp://guest:guest@{rabbitmq_url}:5672")
QUEUE_NAME: str = os.getenv("QUEUE_NAME", "user_registered")

async def on_message(message: IncomingMessage):
    async with message.process():
        user_data = json.loads(message.body)
        send_notification(user_data)

async def start_consumer():
    connection = await connect_robust(RABBITMQ_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue(QUEUE_NAME, durable=True)
    await queue.consume(on_message)
    print(f"Started consuming from '{QUEUE_NAME}' queue...")
    return connection