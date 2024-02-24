import pyrebase
import module.sendEmail as mail
from dotenv import load_dotenv
import os
import uuid  # Import the uuid module


load_dotenv()

# Your Firebase configuration
firebaseConfig = {
  "apiKey":os.getenv("FIREBASE_API_KEY") ,
  "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
  "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
  "projectId": os.getenv("FIREBASE_PROJECT_ID"),
  "storageBucket":os.getenv("FIREBASE_STORAGE_BUCKET"),
  "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
  "appId": os.getenv("FIREBASE_APP_ID"),
  "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
};

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)

# Get a reference to the Firebase database
db = firebase.database()

def create_db_client(data):
    # Check if the email already exists
    existing_emails = db.child('clients').order_by_child('email').equal_to(data['email']).get()
    if existing_emails.each():
        # print("Client with this email already exists.")
        return "Already Registered"

    # Generate a unique ID for the new client
    new_client_id =data['first_name']+str(uuid.uuid4())

    # Add the new client to the database
    # Create a new client with the generated ID
    db.child("clients").child(new_client_id).set(data)
    mail.clients_mail(data)
    # print("Client created successfully")
    return 'Registered Successfully'

def create_db_candidates(data):
    # Check if the email already exists
    existing_emails = db.child('candidates').order_by_child('email').equal_to(data['email']).get()

    if existing_emails.each():
        print("Client with this email already exists.")
        return "Already Registered"

    # Generate a unique ID for the new client
    new_candidate_id =data['name']+str(uuid.uuid4())
    new_candidate_id = new_candidate_id.replace(".", "-")

    print(new_candidate_id)
    
    # Add the new client to the database
    # Create a new client with the generated ID
    db.child("candidates").child(new_candidate_id).set(data)

    mail.candidates_mail(data)
 

    return 'Registered Successfully'
  
  
def SubscribeList(email):
  existing_emails = db.child('subscribers').order_by_child('email').equal_to(email).get()

  if existing_emails.each():
    raise ValueError(f"Email '{email}' already exists in the subscribers list.")
  
  else:
      # Use push() to generate an auto-generated unique ID as the key
    subscriber_ref = db.child('subscribers').push({
          'email': email,
        })
    print(subscriber_ref)
    return 'OK'



# m={'first_name': 'SHYAM', 'last_name': 'T.R', 'email': 't.r.shyam0007@gmail.com', 'phone_number': '07448384181'}
# print(create_db_candidates(m))
# create_db_client()