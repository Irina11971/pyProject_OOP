# Задание 1.
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины,
# цену. Реализуйте конструктор по умолчанию и метод для вывода данных.

class Car:

    def __init__(self, model: str, year_release: int, manufacturer: str, engine_capacity: float, colour: str, price: int):
        """Конструктор класса Car"""
        self.model = model
        self.year_release = year_release
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.colour = colour
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




def execute_application():

    car1 = Car("Volkswagen Caravelle", 2021,"Volkswagen", 2.0, "черный", 4150000)
    car2 = Car("Suzuki SX4", 2011,"Volkswagen", 1.6, "серебристый", 915000)

    cars = []
    cars.append(car1)
    cars.append(car2)
    for car in cars:
        print(car)


if __name__ == "__main__":
    execute_application()




