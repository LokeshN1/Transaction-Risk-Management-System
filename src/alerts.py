# src/alerts.py

import smtplib
from email.mime.text import MIMEText
import ssl # Import the SSL module for a secure connection

def send_alert(recipient_email, subject, message):
    # --- CONFIGURATION ---
    sender_email = "lokeshnegi399@gmail.com" 
    sender_password = "owidtsxojwksmwxo" 
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 465 # For SSL

    # --- CREATE THE EMAIL ---
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # --- SEND THE EMAIL ---
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    print(f"Connecting to {smtp_server} to send email to {recipient_email}...")
    
    # Use smtplib.SMTP_SSL for a secure connection from the start
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")