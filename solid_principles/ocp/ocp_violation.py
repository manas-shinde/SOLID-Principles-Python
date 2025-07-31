class Order:
    def __init__(self, amount: float, order_type: str = None):
        self.amount = amount
        self.order_type = order_type

    def calculate_final_amount(self) -> float:
        if self.discount_type == "percentage":
            return self.amount * 0.9  # 10% discount
        elif self.discount_type == "fixed":
            return self.amount - 50
        else:
            return self.amount
