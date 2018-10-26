from twilio.rest import Client 

account_sid = 'AC3c447286805366dc1c9a31a81dde0fe4'
auth_token = 'ff00f775e60379a7bceca18926b710b2'

client = Client(account_sid, auth_token)

message = client.message.create(
    # Need to get Twilio account number paid 
)
