import sqlite3
from sqlite3 import Error

class User:
    def RegisterUser(self, name, password, email):
        con = sqlite3.connect('user.db')
        sql = f"INSERT INTO Users VALUES ('{name}','{password}','{email}')"
        con.execute(sql)
        con.commit()
        print(f"User Registered with {name} and {email}")

  
# import syslog
# class Logger:
#     def WriteLogToSystem(self, message):
#         syslog.syslog(syslog.LOG_ERR, message)


import json
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email:
    def SendEmail(self, to_email, message_content, subject="User Registered"):
        with open('credentials.json') as f:
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
        message_content = f"Hello, <br/><b>Message from Dark Energy: </b><br/> {message_content} <br/>All The Best<br/>Support Team"
        
        part = MIMEText(message_content, "html")
        
        message.attach(part)

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, to_email, message.as_string())

        print(f"Mail Sent to {to_email}")


# Facade Pattern
class Registrations:
    def RegisterUser(self, username, password, email):
        try:
            User().RegisterUser(username, password, email)
            Email().SendEmail(email, "You have Successfully Registered")
        except Exception:
            print("Error While Registering User")
            # Logger().WriteLogToSystem("Error While Registering User")


register = Registrations()
register.RegisterUser("Prabhu", "prabhu.net", "prabhu.ece001@gmail.com")