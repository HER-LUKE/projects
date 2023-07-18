import smtplib

# Set up variabes
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'example@gmail.com'
SENDER_PASSWORD = 'password'
RECIPIENT_EMAIL = 'example@tmomail.net'
EMAIL_SUBJECT = 'Example Subject'
EMAIL_BODY = 'Example Body'


#set up server, send message, check for errors, close server
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        msg = f'Subject: {EMAIL_SUBJECT}\n\n{EMAIL_BODY}'
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg)
        print('Email sent successfully!')
except smtplib.SMTPAuthenticationError as e:
    print('Failed to authenticate:', e)
except smtplib.SMTPException as e:
    print('An SMTP error occurred:', e)
except Exception as e:
    print('An Error Occured:', e)

