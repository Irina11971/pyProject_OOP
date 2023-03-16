
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



if __name__ == "__main__":
    execute_application()
