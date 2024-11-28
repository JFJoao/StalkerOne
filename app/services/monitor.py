import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

target_url = 'https://alvo.com'
CHECK_INTERVAL = 5
'''
EMAIL = ''
PASSWORD = ''
destinatario = ''

def send_email_notification(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = destinatario
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Change for non-Gmail providers
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()

        print("Notification sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")'''

def website_content(target_url):
    try:
        response = requests.get(target_url)
        response.raise_for_status()
        return response.text  # Return only the content as text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

# comparação
def monitor_website():

    last_content = website_content(target_url)

    if last_content is None:
        return

    while True:
        time.sleep(CHECK_INTERVAL)
        current_content = website_content(target_url)
        if current_content is None:
            continue
        # Compare the new content with the last one
        if current_content != last_content:
            print("Change detected!")
            last_content = current_content

if __name__ == '__main__':
    monitor_website()
