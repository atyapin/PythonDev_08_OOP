from typing import List
from .order import Order

class Customer:
    """
    Клиент с именем и списком заказов.
    """
    def __init__(self, name: str):
        self.name = name
        self.orders: List[Order] = []

    def place_order(self, order: Order):
        self.orders.append(order)

    def total_spent(self) -> float:
        return sum(o.total_price() for o in self.orders)

    def __str__(self):
        return f"Клиент {self.name} (заказов={len(self.orders)}, потрачено={self.total_spent()})"

    def __repr__(self):
        orders_repr = ',\n        '.join(repr(order) for order in self.orders)
        return (f"Customer(\n"
                f"    name={self.name!r},\n"
                f"    orders=[\n"
                f"        {orders_repr}\n"
                f"    ],\n"
                # f"#    total_spent={self.total_spent()}\n"
                f")")