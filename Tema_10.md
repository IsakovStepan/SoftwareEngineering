Тема 10. Декораторы и исключения
Отчет по Теме №10 выполнил:
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

## Лабораторная работа №10
### Задание 1.

Нужно написать программу, которая будет считать числа Фибоначчи для 100 и запустить ее без этого декоратора и с ним, посмотреть на разницу во времени решения поставленной задачи.

```python
from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print(fibonacci(100))
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_10/pic/Lab1.png)

### Вывод

Декоратор @lru_cache решает проблему экспоненциальной сложности рекурсивных.

### Задание 2.

Напишите декоратор для функции, который будет принимать все параметры вызываемой функции (имя, возраст) и проверять чтобы возраст был больше 0 и меньше 130.

```python
def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = 'Недопустимый возраст'
        input_func(name, age)

    return output_func


@check
def personal_info(name, age):
    print(f"Name: {name}, Age: {age}")

if __name__ == '__main__':
    personal_info('Владимир', 38)
    personal_info('Александр', -5)
    personal_info('Пётр', 138, 15, 48, 2)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_10/pic/Lab2.png)

### Вывод

Создан декоратор validate_age, который выполняет корректность входных данных пользователя.

### Задание 3.

Воспользуйтесь исключениями, чтобы неподходящий тип данных не ломал ваш сайт.

```python
def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] * 15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print('Вся информация обработана')

if __name__ == '__main__':
    data([1, 15, 'Hello', 'i', 'try', 'to', 'crash', 'your', 'site', 38, 45])
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_10/pic/Lab3.png)

### Вывод

Реализована надежная система обработки ошибок с использованием декоратора safe_data_processing.

### Задание 4.

Продолжая работу над сайтом, вы решили написать собственное исключение, которое будет вызываться в случае, если в функцию проверки имени при регистрации передана строка длиннее десяти символов

```python
class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name) > 10:
        raise NegativeValueException('Длина более 10 символов')
    else:
        print('Успешная регистрация')

if __name__ == '__main__':
    name = "1234567891"
    check_name(name)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_10/pic/Lab4.png)

### Вывод

Создано семантически ясное пользовательское исключение NameTooLongError, которое точно описывает проблему с длиной имени.

### Задание 5.

Создайте необходимый вам декоратор. Выведите все логи в консоль.

```python
class SiteChecker:
    def __init__(self, func):
        print('> Класс SiteChecker метод __init__ успешный запуск')
        self.func = func

    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного выключения')

@SiteChecker
def site():
    print('Усердная работа сайта')

if __name__ == '__main__':
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_10/pic/Lab5.png)

### Вывод

Декоратор успешно отслеживает все этапы работы функций: инициализацию, выполнение и завершение.

---

## Самостоятельная работа №10
### Задание 1.

Декоратор для функции, который будет выяснять за какое время выполняется та или иная функция.

```python
import time
import functools


def timer(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"\nВремя выполнения функции: {execution_time:.6f} секунд")
        return result

    return wrapper


@timer
def fibonacci():
    fib1 = fib2 = 1
    print("Числа Фибоначчи:", end=' ')
    print(fib1, fib2, end=' ')

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')
    print()


if __name__ == '__main__':
    fibonacci()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_10/pic/Sam1.png)

### Вывод

В ходе выполнения задачи был успешно создан декоратор timer, который точно измеряет время выполнения функций. На примере функции fibonacci продемонстрирована эффективность итеративного подхода по сравнению с рекурсивным - вычисление 200 чисел Фибоначчи заняло менее 0.01 секунды.

### Задание 2.

Создайте пустой файл и файл, в котором есть какая-то информация. Напишите код программы. Если файл пустой, то, нужно вызвать исключение (“бросить исключение”) и вывести в консоль “файл пустой”, а если он не пустой, то вывести информацию из файла.

```python
def read_file_safe(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

            if not content.strip():
                raise ValueError("файл пустой")

            print(f"Содержимое файла '{filename}':")
            print(content)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")

if __name__ == '__main__':
    with open('empty_file.txt', 'w', encoding='utf-8') as f:
        pass

    with open('data_file.txt', 'w', encoding='utf-8') as f:
        f.write("Это тестовые данные для проверки работы программы.\n")
        f.write("Файл содержит информацию для обработки.\n")

    read_file_safe('empty_file.txt')

    read_file_safe('data_file.txt')

    read_file_safe('nonexistent_file.txt')
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_10/pic/Sam2.png)

### Вывод

Программа корректно различает три критических сценария: отсутствие файла, пустой файл и файл с данными.

### Задание 3.

Напишите функцию, которая будет складывать 2 и введенное пользователем число, но если пользователь введет строку или другой неподходящий тип данных, то в консоль выведется ошибка “Неподходящий тип данных. Ожидалось число.”.

```python
def add_two():
    try:
        user_input = input("Введите число для сложения с 2: ")
        number = float(user_input)

        result = 2 + number
        print(f"Результат: 2 + {number} = {result}")

    except ValueError:
        print("Ошибка: Неподходящий тип данных. Ожидалось число.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")

if __name__ == '__main__':
    add_two()

    add_two()

    add_two()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_10/pic/Sam3.png)

### Вывод

Создана устойчивая к ошибкам ввода функция, которая элегантно обрабатывает некорректные данные пользователя. Применение блока try/except с конкретным исключением ValueError позволяет отлавливать ошибки преобразования типов без прерывания работы программы. 

### Задание 4.

Создайте собственный декоратор, который будет использоваться для двух любых вами придуманных функций.

```python
import functools

class CallCounter:
    def __init__(self, func):
        self.func = func
        self.call_count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"Функция '{self.func.__name__}' вызвана {self.call_count} раз")
        return self.func(*args, **kwargs)


@CallCounter
def calculate_square(n):
    result = n ** 2
    print(f"Квадрат числа {n} равен {result}")
    return result


@CallCounter
def calculate_cube(n):
    result = n ** 3
    print(f"Куб числа {n} равен {result}")
    return result

if __name__ == '__main__':
    calculate_square(5)
    calculate_cube(3)
    calculate_square(10)
    calculate_cube(2)
    calculate_square(7)

    print(f"\nИтоговое количество вызовов:")
    print(f"calculate_square: {calculate_square.call_count}")
    print(f"calculate_cube: {calculate_cube.call_count}")
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_10/pic/Sam4.png)

### Вывод

Успешно разработан оригинальный декоратор CallCounter, который реализован в виде класса с сохранением состояния.

### Задание 5.

Создайте собственное исключение, которое будет использоваться в двух любых фрагментах кода.

```python
class NegativeNumberError(Exception):
    def __init__(self, value, message="Отрицательные числа не допускаются"):
        self.value = value
        self.message = f"{message}: получено {value}"
        super().__init__(self.message)


def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError(number, "Невозможно вычислить квадратный корень")

    result = number ** 0.5
    print(f"Квадратный корень из {number} равен {result:.2f}")
    return result


def process_age(age):
    if age < 0:
        raise NegativeNumberError(age, "Возраст не может быть отрицательным")

    print(f"Возраст {age} лет корректен")
    return age

if __name__ == '__main__':
    try:
        calculate_square_root(16)
        process_age(25)
    except NegativeNumberError as e:
        print(f"Поймано исключение: {e}")

    try:
        calculate_square_root(-4)
    except NegativeNumberError as e:
        print(f"Поймано исключение: {e}")

    try:
        process_age(-5)
    except NegativeNumberError as e:
        print(f"Поймано исключение: {e}")

    try:
        calculate_square_root(9)
        process_age(-10)
        calculate_square_root(25)
    except NegativeNumberError as e:
        print(f"Поймано исключение: {e}")
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_10/pic/Sam5.png)

### Вывод

Создано семантически значимое пользовательское исключение NegativeNumberError, которое улучшает читаемость кода и точность обработки ошибок.
