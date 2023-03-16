
# Задание 1.
# Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
# дату рождения, контактный телефон, город, страну, домашний адрес.
# Реализуйте конструктор по умолчанию и метод для вывода данных.


class Human:

    name: str
    date_birth: str
    telephone: str
    country: str
    city: str
    home_address: str

    def __init__(self, name: str, date_birth: str, telephone: str,
                 country: str, city: str, home_address: str):
        """Конструктор класса Human"""
        self.name = name
        self.date_birth = date_birth
        self.telephone = telephone
        self.country = country
        self.city = city
        self.home_address = home_address

    def __str__(self):
        return f"ФИО: {self.name} \n" \
               f"Дата рождения: {self.date_birth} \n" \
               f"Телефон: {self.telephone} \n" \
               f"Страна: {self.country} \n" \
               f"Город: {self.city} \n" \
               f"Домашний адрес: {self.home_address} \n"


def execute_application():


    human1 = Human("Караваев Я.Д.", "03.02.1985", "910-634-03-69", "Россия", "Ярославль", "ул. Бабича, д. 16, кв. 5")
    human2 = Human("Краснов С.Ю.", "25.02.1965", "915-634-10-85", "Россия", "Ярославль", "ул. Космонавтов, д. 1, кв. 9")
    humans = []
    humans.append(human1)
    humans.append(human2)
    for human in humans:
        print(human)


if __name__ == "__main__":
    execute_application()
