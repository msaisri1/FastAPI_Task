import smtplib
from email.message import EmailMessage
import os

SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", 25))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")

def send_email(email, full_name):
    msg = EmailMessage()
    msg["Subject"] = "Welcome to Our App!"
    msg["From"] = "noreply@example.com"
    msg["To"] = email
    msg.set_content(f"Hello {full_name},\n\nThank you for registering with our service!\n\n- The Team")

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            if SMTP_USER and SMTP_PASS:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
            print(f"Email sent to {email}")
    except Exception as e:
        print(f"Failed to send email to {email}: {e}")