from classes import Product, Order, Customer, Discount

def main():
    # 1.	Создайте несколько продуктов и клиентов.
    # Продукты
    p1 = Product("Laptop", 1000)
    p2 = Product("Mouse", 50)
    p3 = Product("Keyboard", 80)
    p4 = Product("Monitor", 250)

    print("============================ Продукты:")
    print(p1)
    print(repr(p2))
    print(p3)
    print(repr(p4))
    print("============================ Продукты")

    # Клиенты
    customer1 = Customer("Ирина")
    customer2 = Customer("Оксана")
    print("============================ Клиенты:")
    print(customer1)
    print(f"{customer2!r}")
    print("============================ Клиенты")

    # сравнение
    print("============================ Сравнение продуктов по цене:")
    print("p2 == p3 ?", p2 == p3)
    print("p2 < p3 ?", p2 < p3)
    print("============================ Сравнение продуктов по цене")

    # 2 Создаём несколько заказов для клиентов, 
    order1 = Order([p1, p2])   # 1000 + 50 = 1050
    order2 = Order([p3, p4])   # 80 + 250 = 330
    order3 = Order([p1, p1])   # 100 + 1000 = 2000

    print("============================ Заказы:")
    print(order1)
    print(repr(order2))
    print(repr(order3))
    print("============================ Заказы")

    # Добавляем заказы клиентам, используя соответствующую функциональность
    customer1.place_order(order1)
    customer1.place_order(order2)
    customer2.place_order(order3)

    print("============================ Все заказы до скидок:")    
    print("Всего заказов (класс):", Order.total_orders())
    print("Сумма всех заказов (класс):", Order.total_value_all_orders())
    print("============================ Все аказы до скидок")    

    # Клиенты с их заказами и итоговыми суммами до применения скидок
    print("============================ Клиенты с их заказами и итоговыми суммами до применения скидок")
    print(customer1)
    print(f"{customer2!r}")
    print("============================ Клиенты с их заказами и итоговыми суммами до применения скидок")


    # 3.	Примените различные типы скидок к заказам.
    seasonal_total, seasonal_percent = Discount.seasonal(order1, 10)
    print(f"Сезонная скидка {seasonal_percent}% для order1: итог = {seasonal_total}")

    promo_total, promo_percent = Discount.promo_code(order2, "VIP20")
    print(f"Промокод применён ({promo_percent}%): итог для order2 = {promo_total}")

    d = Discount("Специальная скидка", 15)
    discounted = Discount.apply_to_order(order1, d.discount_percent)
    print(f"{d}: order1 после скидки = {discounted}")

    # print("============================ Заказы после скидок:")    
    # print("Всего заказов (класс):", Order.total_orders())
    # print("Сумма всех заказов (класс):", Order.total_value_all_orders()) 
    # print("============================ Заказы после скидок")    

    # Клиенты с их заказами и итоговыми суммами после применения скидок
    # print("Клиенты с их заказами и итоговыми суммами после применения скидок")
    # print(customer1)
    # print(f"{customer2!r}")

if __name__ == "__main__":
    main()