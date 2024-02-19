import pyrebase
import module.sendEmail as mail



# Your Firebase configuration
firebaseConfig = {
  "apiKey": "AIzaSyD3zFWGap5FHanA3mhRqH-MVL1vNzhiJyA",
  "authDomain": "virtuospark-b4825.firebaseapp.com",
  "databaseURL": "https://virtuospark-b4825-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "virtuospark-b4825",
  "storageBucket": "virtuospark-b4825.appspot.com",
  "messagingSenderId": "431621447944",
  "appId": "1:431621447944:web:74a72a3dfd6cb32d6c8cbd",
  "measurementId": "G-T0D5PML12W"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)

# Get a reference to the Firebase database
db = firebase.database()

def create_db_client(data):
  print(data)
  existing_user = db.child("clients").child(data['first_name']).get()
  
  if existing_user.val() is None:
    db.child("clients").child(data['first_name']).set(data)
    mail.send_mail(data)
    print("Client created successfully")
    return 'OK'

  else:
    return 'no'

def create_db_candidates(data):
  print(data)
  print(data)
  print(data)
  print(data)
  existing_user = db.child("candidates").child(data['first_name']).get()
  if existing_user.val() is None:
    db.child("candidates").child(data['first_name']).set(data)
    print("Client created successfully")
    return 'User created successfully'
  else:
    return 'User already exists'

def SubscribeList(email):
  existing_emails = db.child('subscribers').order_by_child('email').equal_to(email).get()

  if existing_emails.each():
    raise ValueError(f"Email '{email}' already exists in the subscribers list.")
  else:
      # Use push() to generate an auto-generated unique ID as the key
    subscriber_ref = db.child('subscribers').push({
            'email': email,
        })
    return 'OK'



# m={'first_name': 'SHYAM', 'last_name': 'T.R', 'email': 't.r.shyam0007@gmail.com', 'phone_number': '07448384181'}
# print(create_db_candidates(m))