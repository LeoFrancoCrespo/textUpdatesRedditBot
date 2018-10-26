from twilio.rest import Client 
from twilio_account_information import ACCOUNT_SID, AUTH_TOKEN

client = Client(account_sid, auth_token)

message = client.message.create(
    # Need to get Twilio account number paid 
)
