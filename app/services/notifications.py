import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


EMAIL = 'webmonitor.contact@gmail.com'
PASSWORD = 'kphv ujpc drwt ioba' #@@@@@@@@@ RETIRAR DO CODIGO POSTERIORMENTE !!!!!!!!!!!!!!!!!!
destinatario = 'webmonitor.contact@gmail.com'

def send_email_notification(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = destinatario
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()

        print("Notification sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

send_email_notification("Alerta de monitoramento", "Houve alteração no site @@@inserir variável@@@")

#def send_sms_notification():


#def send_whatsapp_notification():

