import pika
import json
from app.schemas.user import UserOut

def publish_user_registered(user: UserOut):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="user.registration")

    message = json.dumps({
        "email": user.email,
        "full_name": user.full_name,
        "role": user.role
    })
    channel.basic_publish(
        exchange="",
        routing_key="user.registration",
        body=message
    )
    connection.close()