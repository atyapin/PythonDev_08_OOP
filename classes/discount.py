from typing import Tuple
from .order import Order
from .product import Product

class Discount:
    """
    Скидка: описание + процент. Статические методы для применения скидок.
    """
    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = float(discount_percent)

    def __str__(self):
        return f"Скидка ({self.description}: {self.discount_percent}%)"

    def __repr__(self):
        return f"Discount(description={self.description!r}, discount_percent={self.discount_percent})"

    @staticmethod
    def calculate_price(price: float, discount_percent: float) -> float:
        if price < 0:
            raise ValueError("price must be non-negative")
        return price * (1 - discount_percent / 100)

    @staticmethod
    def apply_to_product(product: Product, discount_percent: float) -> float:
        return Discount.calculate_price(product.price, discount_percent)

    @staticmethod
    def apply_to_order(order: Order, discount_percent: float) -> float:
        return Discount.calculate_price(order.total_price(), discount_percent)

    @staticmethod
    def seasonal(order: Order, seasonal_percent: float) -> Tuple[float, float]:
        total = Discount.apply_to_order(order, seasonal_percent)
        return total, seasonal_percent

    @staticmethod
    def promo_code(order: Order, code: str) -> Tuple[float, float]:
        promo_map = {
            "WELCOME10": 10.0,
            "VIP20": 20.0,
            "BLACKFRIDAY": 50.0,
        }
        percent = promo_map.get(code.upper(), 0.0)
        total = Discount.apply_to_order(order, percent)
        return total, percent