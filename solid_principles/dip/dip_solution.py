from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient, message):
        pass


class EmailSender(MessageSender):
    def send_message(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


class SMSSender(MessageSender):
    def send_message(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")
        # Low-level SMS sending logic


class PushNotificationSender(MessageSender):
    def send_message(self, recipient, message):
        print(f"Sending Push Notification to {recipient}: {message}")
        # Low-level SMS sending logic


class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send_notification(self, recipient, message):
        self.sender.send_message(recipient, message)


if __name__ == "__main__":
    email_notifier = NotificationService(EmailSender())
    email_notifier.send_notification("user@example.com", "Your order has shipped!")

    sms_notifier = NotificationService(SMSSender())
    sms_notifier.send_notification("+919876543210", "Your password reset code is 1234.")

    push_notifier = NotificationService(PushNotificationSender())
    push_notifier.send_notification(
        "mobile_device_id_123", "New message from a friend!"
    )
