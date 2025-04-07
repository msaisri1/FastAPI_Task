import pika
import json
from app.schemas.user import UserOut
from loguru import logger
import os

rabbitmq_url = os.getenv("RABBITMQ_HOST", "rabbitmq")

def publish_user_registered(user: UserOut):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_url))
        channel = connection.channel()
        channel.queue_declare(queue="user_registered", durable=True)

        message = json.dumps({
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role
        })
        channel.basic_publish(
            exchange="",
            routing_key="user_registered",
            body=message
        )
    except:
        logger.info(f"Error publishing")
    finally:
        connection.close()