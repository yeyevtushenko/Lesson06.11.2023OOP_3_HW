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