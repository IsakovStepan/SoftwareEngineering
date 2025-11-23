# Тема 11. Итераторы и генераторы.
Отчет по Теме №11 выполнил:
- Исаков Степан Юрьевич
- ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + |  |
| Задание 4 | + |  |
| Задание 5 | + |  |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

---

## Лабораторная работа №11
### Задание 1.

Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть.

```python
numbers = [0, 1, 2, 3, 4, 5]
for item in numbers:
    print(item)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_11/pic/Lab1.png)

### Вывод

Стандартные коллекции Python являются итерируемыми объектами.

### Задание 2.

Класс итератор с гибкой настройкой и удобными применением.

```python
class CountDown:
    def __init__(self, start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count

if __name__ == "__main__":
    counter = CountDown(5)
    for i in counter:
        print(i)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_11/pic/Lab2.png)

### Вывод

Реализован собственный класс-итератор с методами __iter__() и __next__().

### Задание 3.

Генератор списка.

```python
a = [i ** 2 for i in range(1, 5)]

print('a - ', a)
for i in a:
    print(i)

print('iter(a) - ', iter(a))
for i in a:
    print(i)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_11/pic/Lab3.png)

### Вывод

Исследована работа функции iter() со стандартными коллекциями.

### Задание 4.

Выражения генераторы.

```python
b = (i ** 2 for i in range(1, 5))
print(b)
print('first')
for i in b:
    print(i)
print('second')
for i in b:
    print(i)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_11/pic/Lab4.png)

### Вывод

Выражения-генераторы создают итератор, который генерирует значения.

### Задание 5.

Такой же счетчик, как и в первом задании, только это генератор и использует yield.

```python
def countdown(count):
    while count >= 0:
        yield count
        count -= 1

if __name__ == '__main__':
    counter = countdown(5)
    for i in counter:
        print(i)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_11/pic/Lab5.png)

### Вывод

Освоено создание функций-генераторов с использованием ключевого слова yield.

---

## Самостоятельная работа №11
### Задание 1.

Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield

```python
def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = 200
fib_gen = fib(n)
result = None
for _ in range(n):
    result = next(fib_gen)

print(f"Число Фибоначчи под номером {n}: {result}")
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_11/pic/Sam1.png)

### Вывод

Реализована корректная логика последовательного вычисления чисел Фибоначчи

### Задание 2.

К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке.

```python
def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = 200
fib_gen = fib(n)

with open("fib.txt", "w", encoding="utf-8") as file:
    for i, num in enumerate(fib_gen, 1):
        file.write(f"Число Фибоначчи #{i}: {num}\n")

print(f"Все {n} чисел Фибоначчи записаны в файл 'fib.txt'")

fib_gen = fib(n)
for _ in range(n):
    result = next(fib_gen)
print(f"Число Фибоначчи под номером {n}: {result}")
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_11/pic/Sam2.png)
![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_11/pic/Sam2_2.png)

### Вывод

Организована запись всех промежуточных чисел Фибоначчи в файл "fib.txt"
