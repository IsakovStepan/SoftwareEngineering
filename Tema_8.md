# Тема 8. Введение в ООП
Отчет по Теме №8 выполнил:
- Исаков Степан Юрьевич
- ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

---

## Лабораторная работа №8
### Задание 1.

Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

myCar = Car('Toyotta', 'Corolla')
```

### Вывод

В ходе задания был успешно создан класс Car с атрибутами make (производитель) и model (модель).

### Задание 2.

Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

myCar = Car('Toyotta', 'Corolla')
myCar.drive()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_8/pic/Lab2.png)

### Вывод

Класс Car был расширен добавлением метода drive(), который выводит сообщение о движении автомобиля.

### Задание 3.

Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться.

```python
from Lab2 import Car

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()

```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_8/pic/Lab3.png)

### Вывод

Успешно реализовано наследование путем создания класса ElectricCar, который наследует от класса Car.

### Задание 4.

Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу.

```python
class Car:
    def __init__(self, make, model):
        self._make = make
        self.__model = model

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")


my_car = Car("Toyota", "Corolla")
print(my_car._make)
my_car.drive()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_8/pic/Lab4.png)

### Вывод

Реализованы различные уровни доступа к атрибутам.

### Задание 5.

Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади.

```python
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rect = Rectangle(5, 10)
circle = Circle(7)

shapes = [rect, circle]

for shape in shapes:
    print("Площадь фигуры:", shape.area())
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_8/pic/Lab5.png)

### Вывод

Успешно продемонстрирован принцип полиморфизма через создание иерархии классов.

---

## Самостоятельная работа №8
### Задание 1.

Класс и его объект.

```python
class Book:
    def __init__(self, title, author):
        self.title = title # атрибут названия книги
        self.author = author # атрибут автора книги

my_book = Book("Мастер и Маргарита", "Михаил Булгаков")

print(f"Книга: {my_book.title}, Автор: {my_book.author}")
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_8/pic/Sam1.png)

### Вывод

Был создан класс Book. Класс содержит два атрибута: title (название) и author (автор).

### Задание 2.

Атрибуты и методы.

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title  # атрибут названия книги
        self.author = author  # атрибут автора книги
        self.year = year  # новый атрибут - год издания

    def info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")


my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 1966)
my_book.info()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_8/pic/Sam2.png)

### Вывод

Класс Book был расширен путем добавления нового атрибута year (год издания) и метода info().

### Задание 3.

Наследование.

```python
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
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_8/pic/Sam3.png)

### Вывод

Реализовано наследование путем создания класса EBook, который наследует все свойства и методы класса Book.

### Задание 4.

Инкапсуляция.

```python
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
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_8/pic/Sam4.png)

### Вывод

Реализованы три уровня доступа к атрибутам класса.

### Задание 5.

Полиморфизм.

```python
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Гав"

class Cat(Animal):
    def sound(self):
        return "Мяу"

class Cow(Animal):
    def sound(self):
        return "Мууу"

animals = [Dog(), Cat(), Cow()]

print("Звуки животных:")
for i, animal in enumerate(animals, 1):
    print(f"Животное {i}: {animal.sound()}")

print("\nКонкретные животные:")
my_dog = Dog()
my_cat = Cat()
my_cow = Cow()
print(f"Собака говорит: {my_dog.sound()}")
print(f"Кошка говорит: {my_cat.sound()}")
print(f"Корова говорит: {my_cow.sound()}")
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_8/pic/Sam5.png)

### Вывод

Полиморфизм через создание иерархии классов Animal: Dog, Cat, Cow. Каждый класс-потомок переопределяет метод sound(), возвращая уникальное для каждого животного значение.
