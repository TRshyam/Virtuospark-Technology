import smtplib
from email.mime.text import MIMEText

sender_mail_id='t.r.shyam0007@gmail.com'
sender_mail_password='avjl wkxf jvsi aqyg'
receiver_email = "ktraveendran25@gmail.com" #consided as college



def send_mail(data):

    # Set up the email server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Set up the email message
    sender_email = sender_mail_id  #consided as webpage mail
    sender_password=sender_mail_password
    receiver_email = "ktraveendran25@gmail.com" #consided as college
    subject = "New user sign-up request"
    message =f'''
    Username: {data['first_name']}\n 
    last_name:{data['last_name']}\n 
    Email: {data['email']}\n
    phone_number:{data['phone_number']}\n
    
    
    http://127.0.0.1:5000/admin-auth'''

    #organization:{data['organization']}\n   
    # zip_code:{data['zip_code']} \n 
    # state:{data['state']} \n 
    # country:{data['country']} 


    #<<<----- Set up the MIME message ---->>>
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    #<<<----- Set up the MIME message ---->>>


    # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    # Send the email




def sendMail_requi(email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    reciverMail=email
    sender_email = sender_mail_id#consided as webpage mail
    
    sender_password= sender_mail_password
    receiver_email = reciverMail #consided as college
    # print(receiver_email)
    print(sender_email)
    print(sender_email)
    print(sender_email)
    print(sender_email)
    print(sender_password)
    print(sender_password)
    print(sender_password)
    print(sender_password)
    print(sender_password)
    
    subject = "New user sign-up request"
    message=f"'yOU CAN ABLE TO SET PASSWORD THROUGH THIS'  http://127.0.0.1:5000/password?email={receiver_email}"
    print(message)
    #     #<<<----- Set up the MIME message ---->>>
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    #<<<----- Set up the MIME message ---->>>
       # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    # Send the email

    # pass


def send_mes(mes):

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = sender_mail_id#consided as webpage mail
    
    sender_password= sender_mail_password
    receiver_email = "ktraveendran25@gmail.com" #consided as college


    subject = "New user sign-up request"
    message =f'''
    Username: {mes['name']}\n 
    last_name:{mes['number']}\n 
    Message: {mes['message']}\n
    '''
    print(message)
    # #     #<<<----- Set up the MIME message ---->>>
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    #<<<----- Set up the MIME message ---->>>
       # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

# m={'name': 'shyam', 'number': '7448384181', 'message': 'dasdasadsdasdsa'}
# send_mes(m)