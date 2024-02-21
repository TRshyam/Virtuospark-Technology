import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()


sender_mail_id_web=os.getenv("sender_mail_id_web") 
sender_mail_password=os.getenv("sender_mail_password") 
# sender_mail_password='avjl wkxf jvsi aqyg'
client_receiver_email = os.getenv("client_receiver_email") #consided as college
candidates_receiver_email =os.getenv("candidates_receiver_email")  #consided as college



def clients_mail(data):

    # Set up the email server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Set up the email message
    sender_email = sender_mail_id_web  #consided as webpage mail
    sender_password=sender_mail_password
    receiver_email = client_receiver_email #consided as college
    subject = "New user sign-up request"
    message =f'''
    Username: {data['first_name']}\n 
    last_name:{data['last_name']}\n 
    Email: {data['email']}\n
    phone_number:{data['phone_number']}\n
    '''

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



def candidates_mail(data):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = sender_mail_id_web  # replace with your sender email
    sender_password = sender_mail_password  # replace with your sender email password
    receiver_email = candidates_receiver_email  # replace with your receiver email
    
    subject = "New candidate registered"
    
    # Convert the dictionary to a string representation
    message = "\n".join([f"{key}: {value}" for key, value in data.items()])
    
    # Set up the MIME message
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

# Example dictionary
# def send_mes(mes):

#     smtp_server = "smtp.gmail.com"
#     smtp_port = 587
#     sender_email = sender_mail_id_web#consided as webpage mail
    
#     sender_password= sender_mail_password
#     receiver_email = "ktraveendran25@gmail.com" #consided as college


#     subject = "New user sign-up request"
#     message =f'''
#     Username: {mes['name']}\n 
#     last_name:{mes['number']}\n 
#     Message: {mes['message']}\n
#     '''
#     print(message)
#     # #     #<<<----- Set up the MIME message ---->>>
#     msg = MIMEText(message)
#     msg["Subject"] = subject
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#     #<<<----- Set up the MIME message ---->>>
#        # Send the email
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()
#     server.login(sender_email, sender_password)
#     server.sendmail(sender_email, receiver_email, msg.as_string())
#     server.quit()

# # m={'name': 'shyam', 'number': '7448384181', 'message': 'dasdasadsdasdsa'}
# m={'first_name': 'SHYAM T.R', 'email': 't.r.shyam0007@gmail.com', 'phone_number': '+917448384181', 'course_type': 'uiux-development'}
# candidates_mail(m)
# # send_mes(m)