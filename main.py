from datetime import datetime
from email_header import SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_NAME, RECEIVER_EMAIL, EMAIL_SUBJECT, EMAIL_HOST, EMAIL_PORT
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
import smtplib
import locale

if not (EMAIL_HOST and EMAIL_PORT and SENDER_EMAIL and SENDER_PASSWORD and RECEIVER_NAME and RECEIVER_EMAIL and EMAIL_SUBJECT):
    print('Error sending the message.')
    raise Exception("Fill all the email_header file's data.")

locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

CURRENT_DATE = datetime.today().strftime("%d/%m/%Y")

smtp_server = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT)

smtp_server.starttls()

smtp_server.login(SENDER_EMAIL, SENDER_PASSWORD)

try:

    with open('email_message.html', 'r') as email_text:
        with open('hi.jpg', 'rb') as hi_image:
            image = hi_image.read()

        template = Template(email_text.read())

        template = template.substitute(name=RECEIVER_NAME, date=CURRENT_DATE)

        msg = MIMEMultipart()

        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = EMAIL_SUBJECT

        msg.attach(MIMEText(template, 'html'))
        msg.attach(MIMEImage(image, name='hi'))

        smtp_server.send_message(msg)
        smtp_server.quit()

except Exception as e:
    print('Error sending a message.')
    print(e)


print('Message send successfully.')
