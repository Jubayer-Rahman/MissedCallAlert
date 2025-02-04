from flask import request, jsonify
from app.services.abstract_classes.notification_abstract import NotificationAbstract
from app.models.missed_call_alert import MissedCallAlert

class MissedCallAlertController:
    def __init__(self, notification_service: NotificationAbstract):
        self.notification_service = notification_service

    def handle_missed_call_alert(self):
        data = request.get_json()

        # Validate the incoming data
        if not data:
            return jsonify({"status": "error", "message": "No data provided"}), 400

        # Check for required fields
        required_fields = ["caller_number", "call_time", "secondary_phone_number"]
        for field in required_fields:
            if field not in data:
                return jsonify({"status": "error", "message": f"Missing required field: {field}"}), 400

        missed_call_alert = MissedCallAlert(
            caller_number=data["caller_number"],
            call_time=data["call_time"],
            secondary_phone_number=data["secondary_phone_number"]
        )

        message_body = f"Missed call from: {missed_call_alert.caller_number} at {missed_call_alert.call_time}."

        try:
            message_sid = self.notification_service.send_notification(
                message_body, missed_call_alert.secondary_phone_number
            )
            return jsonify({"status": "success", "message_sid": message_sid}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500