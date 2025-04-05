from loguru import logger

def send_notification(user_data:dict):
    logger.info(f"Sending mock email to user: {user_data['email']}")