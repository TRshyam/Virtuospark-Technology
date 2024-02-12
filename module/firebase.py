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
    return 'User created successfully'

  else:
    return 'User already exists'

def create_db_candidates(data):
  existing_user = db.child("candidates").child(data['first_name']).get()
  if existing_user.val() is None:
    db.child("candidates").child(data['first_name']).set(data)
    print("Client created successfully")
    return 'User created successfully'
  else:
    return 'User already exists'




