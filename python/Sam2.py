class Book:
    def __init__(self, title, author, year):
        self.title = title  # атрибут названия книги
        self.author = author  # атрибут автора книги
        self.year = year  # новый атрибут - год издания

    def info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")


my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 1966)
my_book.info()