# Missed Call Alert System

## Project Description
This project is a **Missed Call Alert System** that sends a WhatsApp notification to a secondary phone number whenever a missed call is detected on the primary phone number. It uses **Twilio's WhatsApp API** to send notifications and is built with **Python** and **Flask**.

---

## How It Works
1. **Missed Call Detection**:
   - The system detects missed calls on the primary phone number using **Macrodroid** (an Android automation app).
   - Tasker sends an HTTP POST request to the Flask server with details of the missed call (caller number, call time, and secondary phone number).

2. **WhatsApp Notification**:
   - The Flask server receives the missed call details and uses **Twilio's API** to send a WhatsApp message to the secondary phone number.

3. **Loose Coupling**:
   - The system is designed to be loosely coupled, allowing you to easily replace Twilio with another notification service (e.g., SMS, email) in the future.

---

## How to Set Up the Project

### 1. Prerequisites
- Python 3.x
- Twilio account (with a WhatsApp-enabled phone number)
- Macrodroid (for Android)

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/missed-call-alert.git
cd missed-call-alert
```
### 3. Install Dependencies
Install the required Python packages using the following command:
```bash
pip install -r requirements.txt
```
### 4. Set Up Environment Variables
Create a .env file in the project root and add the following:
```env
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
```
### 5. Run the Flask Application
Start the Flask development server using the following command:
```bash
python run.py
```
### 6. Configure HTTP Request
Configure **Postman** or **Macrodroid** to send an HTTP POST request to your Flask server:
**Method:** POST
**URL:** http://<your-server-ip>:5000/missed-call-alert
**Body:**
```json
{
  "caller_number": "Caller_Num",
  "call_time": "Call_Time",
  "secondary_phone_number": "+1234567890"
}
```
---
### **How to Use:**
1. This project is deployed on the cloud and is accessible at the following URL:
```
https://jubayer150.pythonanywhere.com/.
```
2. Configure Macrodroid on your Android device to send an HTTP POST request to the above URL with the following JSON payload to use the service.
3. Once Macrodroid is configured, any missed calls on your primary phone number will trigger a WhatsApp notification to the specified secondary phone number.
