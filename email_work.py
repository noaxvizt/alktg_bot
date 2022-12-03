from config import LOGIN, PASSWORD
import smtplib
import os
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version
server = 'smtp.yandex.ru'
user = LOGIN
password = PASSWORD


async def send_email(recipient, file_path, theme='АЛКТГ Б05-204 Саидов Саид'):
    recipients = [recipient]
    sender = LOGIN
    subject = theme
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())
    with open(file_path, "rb") as fil:
        part = MIMEApplication(fil.read(), Name=basename(file_path))
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file_path)
    msg.attach(part)
    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()