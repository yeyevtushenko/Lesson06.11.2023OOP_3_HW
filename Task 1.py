# Створіть систему управління замовленнями готелю.
# Кожне замовлення має містити інформацію про клієнта, тип кімнати,
# кількість днів проживання та вартість. Реалізуйте методи для додавання замовлення,
# зміни типу кімнати та кількості днів, а також видалення замовлення.
# Використайте інкапсуляцію для захисту вартості від неправильних змін.
print("Завдання №1")
class HotelOrder:
    def __init__(self, client_name, room_type, stay_days, cost_per_day):
        self.__client_name = client_name
        self.__room_type = room_type
        self.__stay_days = stay_days
        self.__cost_per_day = cost_per_day
        self.__total_cost = stay_days * cost_per_day

    def display_order(self):
        print("Замовлення:")
        print("Клієнт:", self.__client_name)
        print("Тип кімнати:", self.__room_type)
        print("Кількість днів проживання:", self.__stay_days)
        print("Вартість за день:", self.__cost_per_day)
        print("Загальна вартість:", self.__total_cost)

    def update_room_type(self, new_room_type):
        self.__room_type = new_room_type
        print("Тип кімнати оновлено.")

    def update_stay_days(self, new_stay_days):
        self.__stay_days = new_stay_days
        self.__total_cost = new_stay_days * self.__cost_per_day
        print("Кількість днів проживання оновлено.")

    def get_total_cost(self):
        return self.__total_cost

class HotelManagementSystem:
    def __init__(self):
        self.orders = []

    def add_order(self, client_name, room_type, stay_days, cost_per_day):
        new_order = HotelOrder(client_name, room_type, stay_days, cost_per_day)
        self.orders.append(new_order)
        print("Замовлення додано.")

    def display_orders(self):
        print("Список замовлень:")
        for order in self.orders:
            order.display_order()
            print("\n")

    def update_order_room_type(self, order_index, new_room_type):
        if 0 <= order_index < len(self.orders):
            self.orders[order_index].update_room_type(new_room_type)
        else:
            print("Некоректний індекс замовлення.")

    def update_order_stay_days(self, order_index, new_stay_days):
        if 0 <= order_index < len(self.orders):
            self.orders[order_index].update_stay_days(new_stay_days)
        else:
            print("Некоректний індекс замовлення.")

    def remove_order(self, order_index):
        if 0 <= order_index < len(self.orders):
            removed_order = self.orders.pop(order_index)
            print("Замовлення видалено.")
            return removed_order
        else:
            print("Некоректний індекс замовлення.")
            return None

hotel_system = HotelManagementSystem()


hotel_system.add_order("Джон Шевченко", "Single Room", 5, 100)
hotel_system.add_order("Жанна д'Арк", "Double Room", 3, 150)

hotel_system.display_orders()

hotel_system.update_order_room_type(1, "Deluxe Room")
hotel_system.update_order_stay_days(2, 4)

hotel_system.display_orders()

removed_order = hotel_system.remove_order(1)
print("Видалено замовлення:", removed_order)

hotel_system.display_orders()