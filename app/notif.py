# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from twilio.rest.api.v2010.account.message import MessageInstance

from config.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

def send_notif(body: str, from_: str, to: str) -> MessageInstance:
        
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
            body=body,
            from_=from_,
            to=to
        )

    return message
