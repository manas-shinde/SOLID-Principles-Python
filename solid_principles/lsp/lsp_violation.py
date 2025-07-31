class Payment:
    def __init__(self, card_number: str):
        self.card_number = card_number

    def process_payment(self, amount):
        print(f"Processing payment of ${amount:.2f}")

    """_summary_
    with current code, the Payment class is not following the Liskov Substitution Principle (LSP) 
    as it does not allow for different payment methods to be substituted without changing the behavior of the process_payment method.
    """
