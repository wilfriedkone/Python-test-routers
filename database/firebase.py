import firebase_admin
import pyrebase
from configs.firebaseconfig import firebaseConfig

from dotenv import dotenv_values
import json

env = dotenv_values(dotenv_path='.env')

# Initialize Firebase
if not firebase_admin._apps:
    cred = firebase_admin.credentials.Certificate("configs/configkey.json")
    firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# Authentication
authStudent = firebase.auth()

# Pour Stripe, 
stripe_config = json.loads(env['STRIPE_CONFIG'])
stripe_public_key = stripe_config['public_key']
stripe_private_key = stripe_config['private_key']
stripe_price_id = stripe_config['price_id']
stripe_webhook_secret = stripe_config['webhook_secret']