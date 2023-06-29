from twilio.rest import Client

account_sid = 'your twilio accout_sid'  #make sure to enter your accoubt_sid here
auth_token = 'your twilio auth_token'   #make sure to enter your twilio auth_token here
client = Client(account_sid, auth_token)

phone_number = input("Enter your Mobile Number: ")
message_body = input("Enter the message: ")

message = client.messages.create(
    from_="your twilio number",       #make sure to enter your sample number provided by twilio
    body=message_body,
    to=phone_number
)

print("Message sent successfully!")
print("Message SID:", message.sid)
