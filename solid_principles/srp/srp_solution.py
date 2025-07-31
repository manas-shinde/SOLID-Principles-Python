class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def create_user(self):
        print(f"User {self.username} created with email {self.email}")


class UserRepository:
    def save_user_to_db(self, user: User):
        print(f"Saving {user.username} to the database")


class EmailService:
    def send_welcome_email(self, user: User):
        print(f"Sending welcome email to {user.email}")
