import smtplib
from email.mime.text import MIMEText
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from google.oauth2 import service_account

# Load service account details 
try:
    # Credentials you get from registering a new application from gmail
    client_id = application_credential['client_id']
    client_secret = application_credential['client_secret']
    key_file_path = "Project/service_account.json"
    credentials = service_account.Credentials.from_service_account_file(
        key_file_path, scopes = ["https://www.googleapis.com/auth/gmail.send"]
    )

    auth_url, _ = credentials.authorization_grant_url(application_credential["auth_uri"])
    print(auth_url)

    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
except Exception as e:
    print(f"Error loading service account credentials : {e}")
    exit()

# setup the SMTP server with OAuth2
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(client_id, client_secret)

    # Send an email
    sender_email = 'rohanwtson44@gmail.com'
    receiver_email = 'rohan.srivastwa00@gmail.com'

    msg = MIMEText('Hello World! This is a test email.')
    msg['Subject'] = 'Test Email'
    msg['From'] = 'rohanwatson44@gmail.com'
    msg['To'] = 'rohan.srivastwa00@gmail.com'

    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

except Exception as e:
    print(f"Error setting up SMTP client: {e}")
