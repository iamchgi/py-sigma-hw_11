# --------------------------- Homework_6.1  ------------------------------------
"""
Виконав: Григорій Чернолуцький
Модуль роботи з класом 'Книга':


Package Version
------- -------
pip 23.2.1

"""

# Клас книга : номер, автор , назва , видавник, жанр, рік видання
class Book:
    def __init__(self, number, autor, title, publisher, genre, year) -> None:
        self.number = number
        self.author = autor
        self.title = title
        self.publisher = publisher
        self.genre = genre
        self.year = year

    def draw(self) -> None:
        print(f" {self.number} {self.author} \"{self.title}\" \'{self.publisher}\' {self.genre} {self.year} рік")

    def get_number(self) -> int:
        return self.number

    def get_autor(self) -> str:
        return self.author

    def get_title(self) -> str:
        return self.title

    def get_publisher(self) -> str:
        return self.publisher

    def get_genre(self) -> str:
        return self.genre

    def get_year(self) -> int:
        return self.year
