from typing import Dict


# Задание 1.
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины,
# цену. Реализуйте конструктор по умолчанию и метод для вывода данных.
# Реализуйте доступ к отдельным полям класса через методы класса (геттеры и сеттеры).


class Car:

    def __init__(self, model: str, year_release: int, manufacturer: str, engine_capacity: float, colour: str,
                 price: int = None):
        self.__model = model
        self.__year_release = year_release
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__colour = colour
        self.__price = price

    def __str__(self):
        return f"Название модели: {self.__model} \n" \
               f"Год выпуска: {self.__year_release} \n" \
               f"Производитель: {self.__manufacturer} \n" \
               f"Объем двигателя: {self.__engine_capacity} \n" \
               f"Цвет: {self.__colour} \n" \
               f"Цена: {self.__price} \n"

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def year_release(self):
        return self.__year_release

    @year_release.setter
    def year_release(self, year_release: str):
        self.__year_release = year_release

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer

    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, engine_capacity: str):
        self.__engine_capacity = engine_capacity

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour: str):
        self.__colour = colour

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: str):
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
            model = file.readline().rstrip('\n')
            year_release = int(file.readline().rstrip('\n'))
            manufacturer = file.readline().rstrip('\n')
            engine_capacity = float(file.readline().rstrip('\n'))
            colour = file.readline().rstrip('\n')
            price = int(file.readline().rstrip('\n'))
            return cls(model, year_release, manufacturer, engine_capacity, colour, price)


    @staticmethod
    def read_from_file(path: str) -> tuple:
        """
        Считывает объекты класса из файла

        :param path (str): адрес файла
        :return:
            tuple - объект класса
        """
        with open(path, 'r', encoding='UTF-8') as file:
            model = file.readline().rstrip('\n')
            year_release = int(file.readline().rstrip('\n'))
            manufacturer = file.readline().rstrip('\n')
            engine_capacity = float(file.readline().rstrip('\n'))
            colour = file.readline().rstrip('\n')
            price = int(file.readline().rstrip('\n'))
            return model, year_release, manufacturer, engine_capacity, colour, price


# Задание 2.
# Реализуйте класс «Стадион». Необходимо хранить в полях класса:
# название стадиона, дату открытия, страну, город, вместимость. Реализуйте
# конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
# отдельным полям класса через методы класса (геттеры и сеттеры).

class Stadium:

    def __init__(self, name: str, opening_date: Dict[str, str], country: str, city: str, number_seats: int = None):
        """Конструктор класса Stadium"""
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__number_seats = number_seats

    def __str__(self):
        return f"Название стадиона: {self.__name} \n" \
               f"Дата открытия: {list(self.__opening_date.values())} \n" \
               f"Страна: {self.__country} \n" \
               f"Город: {self.__city} \n" \
               f"Вместимость: {self.__number_seats} \n"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def opening_date(self):
        return list(self.__opening_date.values())

    @opening_date.setter
    def opening_date(self, opening_date: Dict[str, str]):
        self.__opening_date = opening_date

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
    def number_seats(self):
        return self.__number_seats

    @number_seats.setter
    def number_seats(self, number_seats: str):
        self.__number_seats = number_seats


    # @classmethod
    # def init_from_file(cls, path: str):
    #     """
    #     Считывает объекты класса из файла
    #
    #     :param path (str): адрес сайта
    #     :return:
    #         str - объект класса
    #     """
    #     with open(path, 'r', encoding='UTF-8') as file:
    #         name = file.readline().rstrip('\n')
    #         opening_date = Dict[str, str]           #??????????????????????
    #         country = file.readline().rstrip('\n')
    #         city = file.readline().rstrip('\n')
    #         number_seats = int(file.readline().rstrip('\n'))
    #         return cls(name, opening_date, country, city, number_seats)
    #
    #
    # @staticmethod
    # def read_from_file(path: str) -> tuple:
    #     """
    #     Считывает объекты класса из файла
    #
    #     :param path (str): адрес файла
    #     :return:
    #         tuple - объект класса
    #     """
    #     with open(path, 'r', encoding='UTF-8') as file:
    #         name = file.readline().rstrip('\n')
    #         opening_date = Dict[str, str]              #?????????????????????
    #         country = file.readline().rstrip('\n')
    #         city = file.readline().rstrip('\n')
    #         number_seats = int(file.readline().rstrip('\n'))
    #
    #         return name, opening_date, country, city, number_seats


def execute_application():
    # Задание 1

    data = Car.read_from_file("file_car.txt")
    car = Car(*data)
    print(car)

    car = Car.init_from_file("file_car.txt")
    print(car)


    # Задание 2

    # stadium1 = Stadium("Стадион 1 мая", {"число": 1, "месяц": "мая", "год": 1989}, "Северная Корея",
    #                    "Пхеньян", 114000)
    # stadium2 = Stadium("Лужники", {"число": 31, "месяц": "июля", "год": 1956}, "Россия",
    #                    "Москва", 76880)
    # stadium3 = Stadium("Камп Ноу", {"число": 24, "месяц": "сентября", "год": 1957}, "Испания",
    #                    "Барселона")
    #
    # stadium1.name = "Олимпийский"
    # stadium1.opening_date = {"число": 1, "месяц": "января", "год": 1111}
    #
    # stadiums = []
    # stadiums.append(stadium1)
    # stadiums.append(stadium2)
    # stadiums.append(stadium3)
    #
    # for stadium in stadiums:
    #     print(stadium)


if __name__ == "__main__":
    execute_application()