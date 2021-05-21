from twilio.rest import Client
import os

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)
    #This class is responsible for sending notifications with the deal flight details.

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=os.environ['TWILIO_NUMBER'],
            to=os.environ['MY_NUMBER']
        )

        print(message.sid)