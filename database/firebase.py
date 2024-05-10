import firebase_admin
import pyrebase
from configs.firebaseconfig import firebaseConfig

from dotenv import dotenv_values
import json
import os
 
from dotenv import load_dotenv
 
load_dotenv()
 
env={
    "FIREBASE_SERVICE_ACCOUNT_KEY": os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY"),
    "FIREBASE_CONFIG": os.getenv("FIREBASE_CONFIG"),
    "STRIPE_CONFIG": os.getenv("STRIPE_CONFIG")
}
 
#from configs.firebase_config import firebase_config
 

# Initialize Firebase
if not firebase_admin._apps:
    cred = firebase_admin.credentials.Certificate(json.loads(config['FIREBASE_SERVICE_ACCOUNT_KEY']))
    firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(json.loads(config['FIREBASE_CONFIG']))
db = firebase.database()

# Authentication
authStudent = firebase.auth()

# Pour Stripe, 
stripe_config = json.loads(env['STRIPE_CONFIG'])
stripe_public_key = stripe_config['public_key']
stripe_private_key = stripe_config['private_key']
stripe_price_id = stripe_config['price_id']
stripe_webhook_secret = stripe_config['webhook_secret']
