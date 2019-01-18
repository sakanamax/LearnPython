# -*- coding: utf-8 -*-
# 程式 11-6 (Python 3 version)
 
import pyrebase,time

config = {
    "apiKey": "AIzaSyCkzoQTc7SVi5EcPq26Tc530ThenywT7n4",
    "authDomain": "nkfust-app.firebaseapp.com",
    "databaseURL": "https://nkfust-app.firebaseio.com",
    "projectId": "nkfust-app",
    "storageBucket": "nkfust-app.appspot.com",
    "messagingSenderId": "276242527307"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("email", "password")

db = firebase.database()

new_users = [
{'name': 'Richard Ho'},
{'name': 'Tom Wu'},
{'name': 'Judy Chen'},
{'name': 'Lisa Chang'}
]

for u in new_users:
    print("Store the data", u)
    db.child('user').push(u, user['idToken'])
    time.sleep(3)
