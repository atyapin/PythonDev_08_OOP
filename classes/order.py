from typing import Iterable
from .product import Product

class Order:
    """
    Класс Order

    Этот класс представляет заказ в интернет-магазине.

    Атрибут класса _total_orders:
        Счетчик всех созданных заказов. Это атрибут класса, а не экземпляра, поэтому он общий для всех объектов Order.

    Метод __init__:
        Конструктор принимает список товаров (products) и инициализирует объект Order.
        Увеличивает счетчик _total_orders на 1 каждый раз при создании нового заказа.
        Пример: order1 = Order([product1]) создаст заказ, содержащий один товар.

    Метод calculate_discounted_price:
        Статический метод, который принимает цену и скидку в процентах и возвращает цену после применения скидки.
        Пример: Order.calculate_discounted_price(1000, 10) вернет 900.0.

    Метод total_orders:
        Метод класса, который возвращает общее количество созданных заказов.
        Пример: Order.total_orders() вернет общее количество заказов.

    Метод total_price:
        Вычисляет общую стоимость всех товаров в заказе, суммируя их цены.
        Пример: order1.total_price() вернет 1000, если в заказе один товар с ценой 1000.

    Метод __str__:
        Возвращает строковое представление объекта заказа, включающее общую стоимость заказа.
        Пример: print(order1) выведет Order(total_price=1000).
    """
    
    _total_orders = 0
    _all_orders = []

    def __init__(self, products: Iterable[Product]):
        # сохраняем копию списка продуктов
        self.products = list(products)
        Order._total_orders += 1
        Order._all_orders.append(self)

    @classmethod
    def total_orders(cls) -> int:
        """    Метод total_orders:
        Метод класса, который возвращает общее количество созданных заказов.
        Пример: Order.total_orders() вернет общее количество заказов.

        Returns:
            int: общее количество созданных заказов
        """
        return cls._total_orders

    @classmethod
    def total_value_all_orders(cls) -> float:
        return sum(o.total_price() for o in cls._all_orders)

    def total_price(self) -> float:
        """
        Метод total_price:
            Вычисляет общую стоимость всех товаров в заказе, суммируя их цены.
            Пример: order1.total_price() вернет 1000, если в заказе один товар с ценой 1000.
    
        Returns:
            float: общую стоимость всех товаров в заказе
        """
        return sum(p.price for p in self.products)

    def __str__(self):
        return f"Заказ (товаров={len(self.products)}, общая_цена={self.total_price()})"

    def __repr__(self):
        prod_repr = ", ".join(repr(p) for p in self.products)
        return f"Order(products=[{prod_repr}], total={self.total_price()})"