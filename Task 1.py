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