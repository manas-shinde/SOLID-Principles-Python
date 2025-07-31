from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        pass


class PercentageDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.9  # 10% discount


class FixedAmountDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount - 50  # Fixed discount of $50


class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.85  # 15% seasonal discount


class Order:
    def __init__(self, amount: float, discount_strategy: DiscountStrategy = None):
        self.amount = amount
        self.discount_strategy = discount_strategy

    def calculate_final_amount(self) -> float:
        if self.discount_strategy:
            return self.discount_strategy.apply_discount(self.amount)
        return self.amount


if __name__ == "__main__":
    try:
        # Usage
        order1 = Order(100)
        print(f"Order 1 final amount: {order1.calculate_final_amount()}")

        order2 = Order(100, PercentageDiscount())
        print(f"Order 2 final amount: {order2.calculate_final_amount()}")

        order3 = Order(100, FixedAmountDiscount())
        print(f"Order 3 final amount: {order3.calculate_final_amount()}")

        order4 = Order(100, SeasonalDiscount())
        print(f"Order 4 final amount: {order4.calculate_final_amount()}")
    except NameError as e:
        print(f"Error occurred: {e}.  Please ensure all classes are defined correctly.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
