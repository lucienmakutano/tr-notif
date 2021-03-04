import os
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY", "unsecure")

SQLALCHEMY_TRACK_MODIFICATIONS=bool(strtobool(os.getenv("SQLALCHEMY_TRACK_MOD", "false")))
SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI")

TWILIO_ACCOUNT_SID=os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN=os.getenv("TWILIO_AUTH_TOKEN")
PHONE_NUMBER=os.getenv("PHONE_NUMBER")
