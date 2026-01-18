import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List

def send_hall_admin_credentials(
        hall_admin_email: str,
        hall_name: str,
        hall_admin_password: str
    ):
    sender_email = os.getenv("SYSTEM_EMAIL")
    sender_password = os.getenv("SYSTEM_EMAIL_PASSWORD")
    receiver_email = hall_admin_email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"Credentials for Hall Admin of {hall_name}"
    body = f"""
    Dear Hall Admin,
    You have been registered as the Hall Admin for {hall_name}.
    Here are your login credentials:
    Email: {hall_admin_email}
    Password: {hall_admin_password}
    Please change your password upon first login.
    Best regards,
    Hallmate Team
    """

    msg.attach(MIMEText(body, 'plain'))
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"Credentials email sent to {hall_admin_email}")
    except Exception as e:
        print(f"Failed to send email to {hall_admin_email}: {e}")