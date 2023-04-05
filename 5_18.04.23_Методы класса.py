from typing import Dict, Tuple

# Задание 1.
# Реализуйте в классе «Человек» дополнительный метод класса и
# статический метод.

class Human:

    def __init__(self, name: str, date_birth: Dict[str, str], telephone: str,
                 country: str, city: str, home_address: Dict[str, str] = None):
        #Конструктор класса Human
        self.__name = name
        self.__date_birth = date_birth.copy()
        self.__telephone = telephone
        self.__country = country
        self.__city = city
        self.__home_address = home_address.copy()

    def __str__(self):
        return f"ФИО: {self.__name} \n" \
               f"Дата рождения: {list(self.__date_birth.values())} \n" \
               f"Телефон: {self.__telephone} \n" \
               f"Страна: {self.__country} \n" \
               f"Город: {self.__city} \n" \
               f"Домашний адрес:{list(self.__home_address.values())} \n"

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

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def home_address(self):
        return list(self.__home_address.values())

    @home_address.setter
    def home_address(self, home_address: Dict[str, str]):
        self.__home_address = home_address.copy()

    @classmethod
    def init_from_file(cls, path: str):
        """
        Считывает объекты класса из файла

        :param path (str): адрес файла
        :return:
            str - объект класса
        """
        with open(path, 'r', encoding='UTF-8') as file:
            name = file.readline().rstrip('\n')
            date_birth_text = file.readline().rstrip('\n').split('.')
            date_birth = dict()
            date_birth["число"] = date_birth_text[0]
            date_birth["месяц"] = date_birth_text[1]
            date_birth["год"] = date_birth_text[2]
            telephone = file.readline().rstrip('\n')
            country = file.readline().rstrip('\n')
            city = file.readline().rstrip('\n')
            home_address_text = file.readline().rstrip('\n').split(",")
            home_address = dict()
            home_address["страна"] = home_address_text[0]
            home_address["город"] = home_address_text[1]
            home_address["улица"] = home_address_text[2]
            home_address["дом"] = home_address_text[3]
            home_address["квартира"] = home_address_text[4]
            return cls(name, date_birth, telephone, country, city, home_address)

    @staticmethod
    def read_from_file(path: str) -> tuple:
        """
        Считывает объекты класса из файла

        :param path (str): адрес файла
        :return:
            tuple - объект класса
        """
        with open(path, 'r', encoding='UTF-8') as file:
            name = file.readline().rstrip('\n')
            date_birth_text = file.readline().rstrip('\n').split('.')
            date_birth = dict()
            date_birth["число"] = date_birth_text[0]
            date_birth["месяц"] = date_birth_text[1]
            date_birth["год"] = date_birth_text[2]
            telephone = file.readline().rstrip('\n')
            country = file.readline().rstrip('\n')
            city = file.readline().rstrip('\n')
            home_address_text = file.readline().rstrip('\n').split(',')
            home_address = dict()
            home_address["страна"] = home_address_text[0]
            home_address["город"] = home_address_text[1]
            home_address["улица"] = home_address_text[2]
            home_address["дом"] = home_address_text[3]
            home_address["квартира"] = home_address_text[4]

            return name, date_birth, telephone, country, city, home_address



# Задание 2.
# Реализуйте в классе «Книга» дополнительный метод класса и
# статический метод.


class Book:
    def __init__(self, title_book: str, year_release: int, publishing_house: str,
                 genre: str, author: str, price: float = None):
        #Конструктор класса Book
        self.__title_book = title_book
        self.__year_release = year_release
        self.__publishing_house = publishing_house
        self.__genre = genre
        self.__author = author
        self.__price = price

    def __str__(self):
        return f"Название книги: {self.__title_book} \n" \
               f"Год выпуска: {self.__year_release} \n" \
               f"Издатель: {self.__publishing_house} \n" \
               f"Жанр: {self.__genre} \n" \
               f"Автор: {self.__author} \n" \
               f"Цена: {self.__price} \n"

    @property
    def title_book(self):
        return self.__title_book

    @title_book.setter
    def title_book(self, title_book: str):
        self.__title_book = title_book

    @property
    def year_release(self):
        return self.__year_release

    @year_release.setter
    def year_release(self, year_release: int):
        self.__year_release = year_release

    @property
    def publishing_house(self):
        return self.__publishing_house

    @publishing_house.setter
    def publishing_house(self, publishing_house: str):
        self.__publishing_house = publishing_house

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre: str):
        self.__genre = genre

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

    @classmethod
    def init_from_file(cls, path: str):
        """
        Считывает объекты класса из файла

        :param path (str): адрес сайта
        :return:
            str - объект класса
        """
        with open(path, 'r', encoding='UTF-8') as file:
            title_book = file.readline().rstrip('\n')
            year_release = int(file.readline().rstrip('\n'))
            publishing_house = file.readline().rstrip('\n')
            genre = file.readline().rstrip('\n')
            author = file.readline().rstrip('\n')
            price = float(file.readline().rstrip('\n'))
            return cls(title_book, year_release, publishing_house, genre, author, price)

    @staticmethod
    def read_from_file(path: str) -> tuple:
        """
        Считывает объекты класса из файла

        :param path (str): адрес файла
        :return:
            tuple - объект класса
        """
        with open(path, 'r', encoding='UTF-8') as file:
            title_book = file.readline().rstrip('\n')
            year_release = int(file.readline().rstrip('\n'))
            publishing_house = file.readline().rstrip('\n')
            genre = file.readline().rstrip('\n')
            author = file.readline().rstrip('\n')
            price = float(file.readline().rstrip('\n'))
            return title_book, year_release, publishing_house, genre, author, price


def execute_application():

    # Задание 1

    # Задание 1
    # Создание экземпляра класса Human с использованием classmethod
    human = Human.init_from_file("file_human.txt")
    print(human)

    # Создание экземпляра класса Human с использованием staticmethod

    data = Human.read_from_file('file_human.txt')
    human = Human(*data)
    print(human)

    # Задание 2

    # Создание экземпляра класса Book с использованием classmethod

    book = Book.init_from_file('file.txt')
    print(book)

    # Создание экземпляра класса Book с использованием staticmethod

    data = Book.read_from_file("file.txt")
    book = Book(*data)
    print(book)


if __name__ == "__main__":
    execute_application()
