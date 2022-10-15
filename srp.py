import smtplib
import sqlite3

class User:
    def register_user(self, username, password, email):
        con = sqlite3.connect('./sqldb.db')
        sql = "INSERT INTO Users VALUES ('{0}', '{1}', '{2}')".format(username, password, email)
        con.execute(sql)
        con.commit()
        print(f"User Registered with {username} and {password}")
    
import logging
class Logger:
    def write_log_to_system(self, message):
        logger = logging.getLogger(__name__)
        logger.error(message)
     
import json
import smtpd, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def send_email(self, to_email, message_content, subject="user registration"):
        with open("credentials.json") as f:
            data = json.load(f)
        
        smtp_server = "smtp.gmail.com"
        port = 465
        sender_email = data["fromuser"]
        password = data["password"]

        context = ssl.create_default_context()
        message = MIMEMultipart("alternative")

        message["From"] = sender_email
        message["To"] = to_email
        message["Subject"] = subject
        message_content = f'Hello, </br><b>Message from Fahad Md Kamal: </b> <br/> \
            {message_content} <br/> All The Best <br/> Best Wishes, <br /> Fahad Md kamal'

        part = MIMEText(message_content, "html")

        message.attach(part)

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, to_email, message.as_string())

        print(f"Mail sent to {to_email}")

class Registerations:
    def register_user(self, username, password, email):
        try:
            User().register_user(username, password, email)
            EmailSender().send_email(email, "You have successfully Registered")
        except Exception:
            Logger().write_log_to_system("Error While Registering User")

r = Registerations()
r.register_user("fahadmdkamal", "12345", "fahadmdkamal@gmail.com")