class Product:
    """
    Класс Product

    Этот класс представляет товар в интернет-магазине.

    Метод __init__:
        Конструктор инициализирует объект Product с двумя атрибутами: name (название товара) и price (цена товара).
        Пример: product1 = Product("Laptop", 1000) создаст товар с названием "Laptop" и ценой 1000.

    Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(product1) выведет Product(name=Laptop, price=1000).
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Продукт (Название={self.name}, Цена={self.price})"

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"

    def __eq__(self, other):
        """Сравнение по цене: равно, если other — Product и цены равны."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price

    def __lt__(self, other):
        """Меньше по цене."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __gt__(self, other):
        """Больше по цене."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price