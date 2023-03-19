# Задание 1.
# Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
# дату рождения, контактный телефон, город, страну, домашний адрес.
# Реализуйте конструктор по умолчанию и метод для вывода данных.
# Реализуйте доступ к отдельным полям класса через методы класса (геттеры и сеттеры).

class Human:

    name: str
    date_birth: Dict[str, str]
    telephone: str
    country: str
    city: str
    home_address: Dict[str, str]

    def __init__(self, name: str, date_birth: Dict[str, str], telephone: str,
                 country: str, city: str, home_address: Dict[str, str]):
        """Конструктор класса Human"""
        self.name = name
        self.date_birth = date_birth
        self.telephone = telephone
        self.country = country
        self.city = city
        self.home_address = home_address

    def __str__(self):
        return f"ФИО: {self.name} \n" \
               f"Дата рождения: {list(self.date_birth.values())} \n" \
               f"Телефон: {self.telephone} \n" \
               f"Страна: {self.country} \n" \
               f"Город: {self.city} \n" \
               f"Домашний адрес: {list(self.home_address.values())} \n"






# Задание 2.
# Реализуйте класс «Книга». Необходимо хранить в полях класса:
# название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте
# конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
# отдельным полям класса через методы класса (геттеры и сеттеры).