class Book:
    def __init__(self, title, author):
        self.title = title      # атрибут названия книги
        self.author = author    # атрибут автора книги

my_book = Book("Мастер и Маргарита", "Михаил Булгаков")

print(f"Книга: {my_book.title}, Автор: {my_book.author}")