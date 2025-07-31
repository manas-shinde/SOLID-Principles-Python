class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def create_user(self):
        print(f"User {self.username} created with email {self.email}")
        self._save_to_db()
        self._send_welcome_email()

    def _save_to_db(self):
        print(f"Saving {self.username} to the database")

    def _send_welcome_email(self):
        print(f"Sending welcome email to {self.email}")
