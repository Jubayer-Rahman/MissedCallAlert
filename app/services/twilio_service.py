from twilio.rest import Client
from app.config.config import Config
from app.services.abstract_classes.notification_abstract import NotificationAbstract

class TwilioService(NotificationAbstract):
    def __init__(self):
        self.client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)

    def send_notification(self, message: str, recipient: str) -> str:
        try:
            message = self.client.messages.create(
                body=message,
                from_=Config.TWILIO_PHONE_NUMBER,
                to=recipient
            )
            return message.sid
        except Exception as e:
            raise Exception(f"Failed to send WhatsApp message: {e}")