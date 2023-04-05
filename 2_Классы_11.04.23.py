# fitcha/task2

from typing import Dict

# Задание 1.
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины,
# цену. Реализуйте конструктор по умолчанию и метод для вывода данных.

class Car:

    def __init__(self, model: str, year_release: int, manufacturer: str, engine_capacity: float, colour: str,
                 price: int = None):
        """Конструктор класса Car"""
        self.model = model
        self.year_release = year_release
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.colour = colour
        if price == None:
            self.price = "не указана"
        else:
            self.price = price


    def __str__(self):
        return f"Название модели: {self.model} \n" \
               f"Год выпуска: {self.year_release} \n"\
               f"Производитель: {self.manufacturer} \n"\
               f"Объем двигателя: {self.engine_capacity} \n"\
               f"Цвет: {self.colour} \n"\
               f"Цена: {self.price} \n"



# Задание 2.
# Реализуйте класс «Стадион». Необходимо хранить в полях класса:
# название стадиона, дату открытия, страну, город, вместимость. Реализуйте
# конструктор по умолчанию и метод для вывода данных.

class Stadium:

    def __init__(self,name: str, opening_date: Dict[str, str], country: str, city: str, number_seats: int = None):
        """Конструктор класса Stadium"""
        self.name = name
        self.opening_date = opening_date.copy()
        self.country = country
        self.city = city
        if number_seats == None:
            self.number_seats = "не указана"
        else:
            self.number_seats = number_seats
    def __str__(self):
        return f"Название стадиона: {self.name} \n" \
               f"Дата открытия: {list(self.opening_date.values())} \n"\
               f"Страна: {self.country} \n"\
               f"Город: {self.city} \n"\
               f"Вместимость: {self.number_seats} \n"




def execute_application():
    """
    # Задание 1

    car1 = Car("Volkswagen Caravelle", 2021,"Volkswagen", 2.0, "черный", 4150000)
    car2 = Car("Suzuki SX4", 2011,"Volkswagen", 1.6, "серебристый")

    cars = []
    cars.append(car1)
    cars.append(car2)
    for car in cars:
        print(car)
    """

    # Задание 2

    stadium1 = Stadium("Стадион 1 мая", {"число": 1, "месяц": "мая", "год": 1989}, "Северная Корея",
                       "Пхеньян", 114000)
    stadium2 = Stadium("Лужники", {"число": 31, "месяц": "июля", "год": 1956}, "Россия",
                       "Москва", 76880)
    stadium3 = Stadium("Камп Ноу", {"число": 24, "месяц": "сентября", "год": 1957}, "Испания",
                       "Барселона")

    stadiums = []
    stadiums.append(stadium1)
    stadiums.append(stadium2)
    stadiums.append(stadium3)

    for stadium in stadiums:
        print(stadium)


if __name__ == "__main__":
    execute_application()




