def send_notificition(channel, data):
    if channel == "email":
        print(f"Sending email notification with data: {data}")
    elif channel == "sms":
        print(f"Sending SMS notification with data: {data}")
    elif channel == "push":
        print(f"Sending push notification with data: {data}")            


send_notificition("email", {"subject": "Test Email", "body": "This is a test email notification."})
send_notificition("sms", {"message": "This is a test SMS notification."})
send_notificition("push", {"title": "Test Push", "message": "This is a test push notification."})