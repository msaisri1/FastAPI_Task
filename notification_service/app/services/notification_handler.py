from loguru import logger
import smtplib
from app.services.email_handler import send_email


def send_notification(user_data:dict):
    send_email(user_data['email'], user_data['full_name'])
    logger.info(f"Sending mock email to user: {user_data['email']}")