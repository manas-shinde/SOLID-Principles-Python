class EmailSender:
    def send_email(self, recipient: str, message: str):
        print(f"Sending email to {recipient}: {message}")


class SMSSender:
    def send_sms(self, phone_number: int, message: str):
        print(f"Sending SMS to {phone_number}: {message}")


class NotificationService:
    def __init(self):
        self.email_sender = EmailSender()
        self.sms_sender = SMSSender()

    def send_notification(self, recipient_type: str, recipient: str, message: str):
        if recipient_type == "sms":
            self.sms_sender.send_sms(recipient, message)
        elif recipient_type == "email":
            self.email_sender.send_email(recipient, message)

        """_summary_
        The NotificationService (high-level module) directly depends on EmailSender and SMSSender (low-level modules).
        If we add a new notification type (e.g., push notification), we modify NotificationService.
        """
