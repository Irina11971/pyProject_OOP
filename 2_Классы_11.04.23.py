# Задание 1.
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины,
# цену. Реализуйте конструктор по умолчанию и метод для вывода данных.

class Car:

    def __init__(self, model: str, year_release: int, manufacturer: str, engine_capacity: int, colour: str, price: int):
        """Конструктор класса Car"""
        self.model = model
        self.year_release = year_release
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.colour = colour
        self.price = price








# Задание 2.
# Реализуйте класс «Стадион». Необходимо хранить в полях класса:
# название стадиона, дату открытия, страну, город, вместимость. Реализуйте
# конструктор по умолчанию и метод для вывода данных.