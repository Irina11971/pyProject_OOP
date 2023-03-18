from typing import Dict

# Задание 1.
# Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
# дату рождения, контактный телефон, город, страну, домашний адрес.
# Реализуйте конструктор по умолчанию и метод для вывода данных.


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


def execute_application():


    human1 = Human("Караваев Я.Д.", {"число": "12", "месяц": "11", "год": "1985"}, "+7 910-634-03-69", "Россия", "Ярославль",
                   {"страна": "Россия", "населенный пункт": "Ярославль", "улица": "Кудрявцева", "дом": 5, "квартира": 86})
    human2 = Human("Краснов С.Ю.", {"число": "3", "месяц": "12", "год": "1998"}, "+7 915-634-10-85", "Россия", "Ярославль",
                   {"страна": "Россия", "населенный пункт": "Ярославль", "улица": "Нахимсона", "дом": 15, "квартира": 8})
    humans = []
    humans.append(human1)
    humans.append(human2)
    for human in humans:
        print(human)


if __name__ == "__main__":
    execute_application()



# Задание 2.
# Реализуйте класс «Книга». Необходимо хранить в полях класса:
# название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте
# конструктор по умолчанию и метод для вывода данных.

class Book:
    title_book: str
    year_release: int
    publishing_house: str
    genre: str
    author: str
    price: float

    def __init__(self, title_book: str, year_release: int, publishing_house: str,
                 genre: str, author: str, price: float):
        """Конструктор класса Book"""
        self.title_book = title_book
        self.year_release = year_release
        self.publishing_house = publishing_house
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return f"Название книги: {self.title_book} \n" \
               f"Год выпуска: {self.year_release} \n" \
               f"Издатель: {self.publishing_house} \n" \
               f"Жанр: {self.genre} \n" \
               f"Автор: {self.author} \n" \
               f"Цена: {self.price} \n"


def execute_application():
    book1 = Book("Изучаем программирование на Python", 2022, "ООО Издательство 'Эксмо'", "Учебник", "Бэрри Пол", 2564.25)
    book2 = Book("Грешник", 2023, "ООО Издательство 'Эксмо'", "Романтическая проза", "Эмма Скотт", 581.65)
    library = []
    library.append(book1)
    library.append(book2)
    for book in library:
        print(book)


if __name__ == "__main__":
    execute_application()
