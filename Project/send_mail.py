# code to send mail to the user 

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_mail(email):
    # The mail addresses and password
    sender_address = 'rohanwatson44@gmail.com'  
    sender_pass =  'Rohan_S@3003' 
    # q: what is sender_pass?
    # a: sender_pass is the password of the sender's email id

    receiver_address = email
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'This mail is sent from Python script'

    # The body and the attachments for the mail
    mail_content = '''Hello Developer,
    This mail is generated by your BAAP of coding in 10s with GitHub co-piolet.'''
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
   

send_mail('rohan.srivastwa00@gmail.com')