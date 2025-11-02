class Book:
    def __init__(self, title, author, year):
        self.title = title  # публичный атрибут
        self._author = author  # защищённый атрибут (одно подчёркивание)
        self.__year = year  # приватный атрибут (два подчёркивания)

    def get_year(self):
        return self.__year

    def info(self):
        print(f"Книга: {self.title}, Автор: {self._author}, Год: {self.__year}")

my_book = Book("1984", "Джордж Оруэлл", 1949)

print("Название (публичный):", my_book.title)
print("Автор (защищённый):", my_book._author)


print("Год через метод:", my_book.get_year())
my_book.info()