class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def download(self):
        print(f"Скачивание книги '{self.title}', размер: {self.file_size} МБ")


my_ebook = EBook("Преступление и наказание", "Фёдор Достоевский", 1866, 2.5)

my_ebook.info()
my_ebook.download()