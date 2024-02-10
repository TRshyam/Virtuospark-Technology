import pyrebase
import module.sendEmail as mail
from flask import flash


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
  
  if existing_user is None:
    db.child("clients").child(data['first_name']).set(data)
    print("Client created successfully")
    return 'User created successfully'

  else:
    return 'User already exists'



# # Example data
# def data():
#     data = {
#         "full_name": "John Doe",
#         "email": "john.doe@example.com",
#         "phone_number": "1234567890",
#         "password": "securepassword",
#         "options": "",
# }

# def create_db(data):   

#     # print(data)
#     user_data=data.copy()
#     user_data.pop('user_id')
#     # print(data['user_id'])
#     # print(user_data)
#     db.child("company_users").child(data['user_id']).set(user_data)
#     print("fb created")
#     print("fb created")
#     print("fb created")
#     print("fb created")
#     print("fb created") 

# # Push the data to the database
# db.child("users").push(data)

# print("Data successfully pushed to the database.")

