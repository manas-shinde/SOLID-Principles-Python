from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def process_payment(self, amount: float) -> str:
        return f"Processing credit card payment of ${amount:.2f} with card {self.card_number}"


class PaypalPayment(PaymentMethod):
    def __init__(self, email: str):
        self.email = email

    def process_payment(self, amount: float) -> str:
        return f"Processing PayPal payment of ${amount:.2f} for {self.email}"


class BankTransferPayment(PaymentMethod):
    def __init__(self, account_number: str):
        self.account_number = account_number

    def process_payment(self, amount: float) -> str:
        return f"Processing bank transfer payment of ${amount:.2f} to account {self.account_number}"


if __name__ == "__main__":
    try:
        # Usage
        payment1 = CreditCardPayment("1234-5678-9012-3456")
        print(payment1.process_payment(100.00))

        payment2 = PaypalPayment("user@example.com")
        print(payment2.process_payment(200.00))

        payment3 = BankTransferPayment("987654321")
        print(payment3.process_payment(300.00))
    except NameError as e:
        print(f"Error occurred: {e}. Please ensure all classes are defined correctly.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
