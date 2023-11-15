# Розробіть систему управління замовленнями таксі.
# Кожне замовлення має містити інформацію про клієнта, адресу, тип автомобіля та вартість.
# Реалізуйте методи для додавання нових замовлень, зміни адреси та типу автомобіля, а також видалення замовлення.
# Використайте інкапсуляцію для захисту вартості від неправильних змін.
print("Завдання №2")
class TaxiOrder:
    def __init__(self, client_name, address, car_type, cost):
        self.__client_name = client_name
        self.__address = address
        self.__car_type = car_type
        self.__cost = cost

    def display_order(self):
        print("Інформація про замовлення:")
        print("Клієнт: ", self.__client_name)
        print("Адреса: ", self.__address)
        print("Тип автомобіля: ", self.__car_type)
        print("Вартість: ", self.__cost)

    def update_address(self, new_address):
        self.__address = new_address
        print("Адресу замовлення оновлено.")

    def update_car_type(self, new_car_type):
        self.__car_type = new_car_type
        print("Тип автомобіля оновлено.")

    def get_cost(self):
        return self.__cost


class TaxiManagementSystem:
    def __init__(self):
        self.orders = []

    def add_order(self, client_name, address, car_type, cost):
        new_order = TaxiOrder(client_name, address, car_type, cost)
        self.orders.append(new_order)
        print("Замовлення таксі додано.")

    def display_orders(self):
        print("Список замовлень таксі:")
        for order in self.orders:
            order.display_order()
            print("\n")

    def update_order_address(self, order_index, new_address):
        if 0 <= order_index < len(self.orders):
            self.orders[order_index].update_address(new_address)
        else:
            print("Некоректний індекс замовлення.")

    def update_order_car_type(self, order_index, new_car_type):
        if 0 <= order_index < len(self.orders):
            self.orders[order_index].update_car_type(new_car_type)
        else:
            print("Некоректний індекс замовлення.")

    def remove_order(self, order_index):
        if 0 <= order_index < len(self.orders):
            removed_order = self.orders.pop(order_index)
            print("Замовлення таксі видалено.")
            return removed_order
        else:
            print("Некоректний індекс замовлення таксі.")
            return None



