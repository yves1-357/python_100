import os
from twilio.rest import Client

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = "+32487328261"

if not ACCOUNT_SID or not AUTH_TOKEN or not TWILIO_NUMBER:
    raise ValueError(
        "Definis TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN et TWILIO_NUMBER "
        "comme variables d'environnement avant de lancer le script."
    )

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="Yello est-tu bien normal.",
    from_=TWILIO_NUMBER,
    to=MY_NUMBER,
)

print(message.sid)
print(message.status)