from flask import Flask
from app.controllers.missed_call_alert_controller import MissedCallAlertController
from app.services.twilio_service import TwilioService

def create_app():
    app = Flask(__name__)

    # Initialize the notification service
    notification_service = TwilioService()

    # Initialize the controller with the chosen service
    missed_call_controller = MissedCallAlertController(notification_service)

    # Register routes
    app.add_url_rule(
        '/missed-call-alert',
        'handle_missed_call_alert',
        missed_call_controller.handle_missed_call_alert,
        methods=['POST']
    )

    return app