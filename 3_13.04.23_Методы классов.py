from typing import Dict

# Задание 1.
# Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
# дату рождения, контактный телефон, город, страну, домашний адрес.
# Реализуйте конструктор по умолчанию и метод для вывода данных.
# Реализуйте доступ к отдельным полям класса через методы класса (геттеры и сеттеры).

class Human:

    def __init__(self, name: str, date_birth: Dict[str, str], telephone: str,
                 country: str, city: str, home_address: Dict[str, str]):
        #Конструктор класса Human
        self.__name = name
        self.__date_birth = date_birth.copy()
        self.__telephone = telephone
        self.country = country
        self.__city = city
        self.home_address = home_address.copy()

    def __str__(self):
        return f"ФИО: {self.__name} \n" \
               f"Дата рождения: {list(self.__date_birth.values())} \n" \
               f"Телефон: {self.__telephone} \n" \
               f"Страна: {self.country} \n" \
               f"Город: {self.__city} \n" \
               f"Домашний адрес:{list(self.home_address.values())} \n"

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def date_birth(self):
        return list(self.__date_birth.values())
    @date_birth.setter
    def date_birth(self, date_birth: Dict[str, str]):
        self.__date_birth = date_birth.copy()

    @property
    def telephone(self):
        return self.__telephone
    
    @telephone.setter
    def telephone(self, telephone: str):
        self.__telephone = telephone

def execute_application():


    human1 = Human("Караваев Я.Д.", {"число": "12", "месяц": "11", "год": "1985"}, "+7 910-634-03-69", "Россия", "Ярославль",
                   {"страна": "Россия", "населенный пункт": "Ярославль", "улица": "Кудрявцева", "дом": 5, "квартира": 86})
    human2 = Human("Краснов С.Ю.", {"число": "3", "месяц": "12", "год": "1998"}, "+7 915-634-10-85", "Россия", "Ярославль",
                   {"страна": "Россия", "населенный пункт": "Ярославль", "улица": "Нахимсона", "дом": 15, "квартира": 8})

    human1.name = "Чернов Я.Д."
    print(human1.name)

    human1.date_birth = ({"число": "1", "месяц": "1", "год": "1985"})  
    print(human1.date_birth)

    human2.name = "Стрельцов О.Н."
    human2.city = "Париж"
    print(human2.city)
    print()

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
# конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
# отдельным полям класса через методы класса (геттеры и сеттеры).
"""

class Book:
    def __init__(self, title_book: str, year_release: int, publishing_house: str,
                 genre: str, author: str, price: float):
        #Конструктор класса Book
        self.__title_book = title_book
        self.__year_release = year_release
        self.publishing_house = publishing_house
        self.genre = genre
        self.__author = author
        self.__price = price

    def __str__(self):
        return f"Название книги: {self.__title_book} \n" \
               f"Год выпуска: {self.__year_release} \n" \
               f"Издатель: {self.publishing_house} \n" \
               f"Жанр: {self.genre} \n" \
               f"Автор: {self.__author} \n" \
               f"Цена: {self.__price} \n"


    @property
    def title_book(self):
        return self.__title_book
    @title_book.setter
    def title_book(self, title_book: str):
        self.__title_book = title_book

    @ property
    def year_release(self):
        return self.__year_release
    @year_release.setter
    def year_release(self, year_release: int):
        self.__year_release = year_release

    @property
    def autor(self):
        return self.__author
    @autor.setter
    def autor(self, autor: str):
        self.__author = autor

    @property
    def price(self):
        return self.__price
        
    @price.setter
    def price(self, price: float):
        self.__price = price


def execute_application():
    book1 = Book("Изучаем программирование на Python", 1022, "ООО Издательство 'Эксмо'", "Учебник", "Бэрри По", 2564.25)
 
    book1.title_book = "Буратино"
    book1.year_release = 2023
    book1.price = 2022
    book1.autor = "Бэрри Пол"

    print(book1)



if __name__ == "__main__":
    execute_application()
