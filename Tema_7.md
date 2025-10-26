# Тема 7. Работа с файлами(ввод, вывод)
Отчет по Теме №7 выполнил:
- Исаков Степан Юрьевич
- ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |  |
| Задание 7 | + |  |
| Задание 8 | + |  |
| Задание 9 | + |  |
| Задание 10 | + |  |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

---

## Лабораторная работа №7
### Задание 1.

Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Lab1.png)

### Вывод

Создан текстовый файл с двумя строками, расположенный в одной папке с программой.

### Задание 2.

Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt','r')
print(f.readline())
f.close()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Lab2.png)

### Вывод

Программа должна открыть файл с помощью open(), прочитать и вывести первую строку, после чего закрыть файл с помощью close().

### Задание 3.

Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('input.txt','r')
print(f.readlines())
f.close()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Lab3.png)

### Вывод

Необходимо прочитать все строки файла в список (массив) с использованием open() и close().

### Задание 4.

Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    print(f.readlines())
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Lab4.png)

### Вывод

Требуется прочитать все строки файла в массив, используя конструкцию with open(), которая обеспечивает автоматическое закрытие файла.

### Задание 5.

Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Lab5.png)

### Вывод

Программа должна выводить каждую строку файла отдельно, используя with open().

### Задание 6.

Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Lab6.png)

### Вывод

Необходимо добавить новую строку в файл (режим 'a' или 'a+'), затем вывести обновлённое содержимое и убедиться, что изменения сохранены в файле.

### Задание 7.

Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Lab7.png)

### Вывод

Требуется полностью перезаписать файл новыми данными (режим 'w'), используя произвольный список строк. После выполнения нужно проверить, что исходные данные заменены.

### Задание 8.

Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит: ')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-'*40)

print_docs('D:\PythonProjects\Laba4')
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Lab8.png)

### Вывод

Нужно написать функцию print_docs(directory), которая выводит содержимое указанной папки и всех её подкаталогов, используя os.walk().

### Задание 9.

Документ «input.txt» содержит следующий текст: Приветствие Спасибо Извините Пожалуйста До свидания Ты готов? Как дела? С днем рождения! Удача! Я тебя люблю. Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных.

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Lab9.png)

### Вывод

Программа должна найти слово (или слова) максимальной длины в файле «input.txt». Результат — слово или список слов, если их несколько.

### Задание 10.

Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
- № - номер по порядку (от 1 до 300);
- Секунда – текущая секунда на вашем ПК;
- Микросекунда – текущая миллисекунда на часах.

Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open('rown_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
    time.sleep(0.01)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Lab10.png)

### Вывод

На каждой итерации добавляется задержка time.sleep(0.01). Данные записываются с помощью модуля csv.

---

## Самостоятельная работа №7
### Задание 1.

Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
from collections import Counter

with open("article.txt", encoding="utf-8") as f:
    text = f.read().lower().split()

word_count = len(text)
most_common = Counter(text).most_common(1)[0]

print(f"Количество слов: {word_count}")
print(f"Самое частое слово: '{most_common[0]}'")
print(f"Количество повторений встречается: {most_common[1]} раз(а)")
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Sam1.png)

### Вывод

Программа успешно определяет общее количество слов и находит наиболее часто встречающиеся слова, что демонстрирует практическое применение словарей и счетчиков для анализа текстовой информации.

### Задание 2.

У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
def add_expense(filename):
    category = input("Категория: ")
    amount = float(input("Сумма: "))
    note = input("Комментарий: ")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{category},{amount},{note}\n")

def show_expenses(filename):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            category, amount, note = line.strip().split(",")
            print(f"{category}: {amount} руб. - {note}")

if __name__ == "__main__":
    add_expense("expenses.txt")
    print("\nТекущие расходы:")
    show_expenses("expenses.txt")
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Sam2.png)

### Вывод

Освоены принципы работы с структурированными данными, сериализацией и организацией интерактивного меню для взаимодействия с пользователем.

### Задание 3.

Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту:
- количество букв латинского алфавита;
- число слов;
- число строк.

Текст в файле:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Ожидаемый результат: Input file contains: 108 letters 20 words 4 lines.

```python
def analyze_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    letters = sum(1 for char in text if char.isalpha())

    words = len(text.split())

    lines = text.count('\n') + 1 if text else 0

    print(f" {letters} letters")
    print(f" {words} words")
    print(f" {lines} lines")

analyze_file("input.txt")
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Sam3.png)

### Вывод

Программа эффективно подсчитывает буквы, слова и строки, демонстрируя различные подходы к обработке строковых данных и работу с файлами построчного чтения. Особое внимание уделено корректной обработке символов и подсчету элементов.

### Задание 4.

Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра

```python
import re

with open("input.txt", encoding="utf-8") as f:
    banned = f.read().split()

text = """Hello, world! Python IS the programming language of thE future. 
My EMAIL is.... 
PYTHON is awesome!!!!"""

for word in banned:
    pattern = re.compile(word, re.IGNORECASE)
    text = pattern.sub("*" * len(word), text)

print(text)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Sam4.png)

### Вывод

Решена задача обработки естественного языка с сохранением структуры исходного текста.

### Задание 5.

Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

```python
def word_statistics():
    filename = input("Введите имя файла: ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        words = text.split()

        total_words = len(words)
        total_chars = sum(len(word) for word in words)
        avg_word_length = total_chars / total_words if total_words > 0 else 0

        longest_word = max(words, key=len) if words else ""

        print(f"\nСтатистика файла '{filename}':")
        print(f"Количество слов: {total_words}")
        print(f"Общее количество символов: {total_chars}")
        print(f"Средняя длина слова: {avg_word_length:.1f}")
        print(f"Самое длинное слово: '{longest_word}'")

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")

word_statistics()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_7/pic/Sam5.png)

### Вывод

Самостоятельно разработана программа анализа текстовой статистики, которая расширяет функционал базового анализа из задачи 3. Добавлены расчет средней длины слова и поиск самого длинного слова, что демонстрирует умение создавать комплексные решения для обработки текстовых данных.
