from loguru import logger
import smtplib
from email.message import EmailMessage

def send_email(email, full_name):
    msg = EmailMessage()
    msg["Subject"] = "Welcome to Our App!"
    msg["From"] = "noreply@example.com"
    msg["To"] = email
    msg.set_content(f"Hello {full_name},\n\nThank you for registering with our service!\n\n- The Team")

    try:
        with smtplib.SMTP("localhost") as server:
            server.send_message(msg)
            print(f"Email sent to {email}")
    except Exception as e:
        print(f"Failed to send email to {email}: {e}")


def send_notification(user_data:dict):
    send_email(user_data['email'], user_data['full_name'])
    logger.info(f"Sending mock email to user: {user_data['email']}")