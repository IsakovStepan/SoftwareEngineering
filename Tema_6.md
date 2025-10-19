# Тема 6. Базовые коллекции: словари, кортежи.
Отчет по Теме №6 выполнил:
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

## Лабораторная работа №6
### Задание 1.

При написании программы необходимо использовать словарь (dict), который на вход получает номер кабинета, а выводит необходимую информацию. Если кабинета, который вы ввели нет в словаре, то в консоль в виде значения ключа нужно вывести “None” и виде статуса вывести “False”.

```python
request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False},
}

response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_6/pic/Lab1.png)

### Вывод

Использование метода get() для безопасного доступа к значениям и обработка отсутствующего ключа через запасной вариант (None) показывает важность обработки крайних случаев.

### Задание 2.

Алексей решил создать самый большой словарь в мире. Для этого он придумал функцию dict_maker (**kwargs), которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict, состоящий всего из одного элемента «first» со значением «so easy». Помогите Алексею создать данную функцию.

```python
from pprint import pprint
my_dict = {'first':'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1=1, a2=20, a3=54, a4= 13)
dict_maker(name='Stepan', age=20, weight=80, eyes_color='blue')
pprint(my_dict)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_6/pic/Lab2.png)

### Вывод

Задача иллюстрирует мощь механизма **kwargs для работы с произвольным количеством именованных аргументов. Метод update() словаря позволяет компактно добавлять множественные элементы. Использование модуля pprint для красивого вывода больших словарей - ценный практический навык для отладки и анализа данных.

### Задание 3.

Для решения некоторых задач бывает необходимо разложить строку на отдельные символы. Мы знаем что это можно сделать при помощи split(), у которого более гибкая настройка для разделения для этого, но если нам нужно посимвольно разделить строку без всяких условий, то для этого мы можем использовать кортежи (tuple).

```python
input_string = 'HelloWorld'
result=tuple(input_string)
print(result)
print(list(result))
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_6/pic/Lab3.png)

### Вывод

Задача показывает альтернативный способ разбиения строки на символы с помощью преобразования в кортеж. Этот подход демонстрирует гибкость преобразований между различными типами коллекций (строка - кортеж - список) и их взаимозаменяемость в определенных сценариях.

### Задание 4.

Вовочка решил написать крутую функцию, которая будет писать имя, возраст и место работы, но при этом на вход этой функции будет поступать кортеж. Помогите Вовочке написать эту программу.

```python
def personal_info(name, age, company='unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

tom = ("Григорий", 22)
personal_info(*tom)

bob = ("Георгий", 41, "Yandex")
personal_info(*bob)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_6/pic/Lab4.png)

### Вывод

Задача отражает важный аспект работы с кортежами - распаковку (unpacking) элементов. Этот механизм позволяет элегантно работать с структурированными данными, извлекать отдельные элементы и использовать их в различных контекстах, что особенно полезно при обработке записей о пользователях.

### Задание 5.

Для сопровождения первых лиц государства X нужен кортеж, но никто не может определиться с порядком машин, поэтому вам нужно написать функцию, которая будет сортировать кортеж, состоящий из целых чисел по возрастанию, и возвращает его. Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.

```python
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((5,5,3,1,9)))
    print(tuple_sort((5,5,2.1,'1',9)))
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_6/pic/Lab5.png)

### Вывод

Задача подчеркивает принцип неизменяемости кортежей и необходимость их преобразования для модификации. Использование isinstance() для проверки типов данных и условного возврата исходного кортежа при наличии нецелочисленных элементов показывает важность валидации входных данных в реальных приложениях.

---

## Самостоятельная работа №6
### Задание 1.

При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные вам форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте вашу задумку. Для получения начальных данных используйте input(). Результатом программы будет выведенный список и кортеж из начальных данных.

```python
def Sam1():
    data = input("Введите числа через пробел: ")

    numbers_list = [int(x) for x in data.split()]
    numbers_tuple = tuple(numbers_list)

    print("Список:", numbers_list)
    print("Кортеж:", numbers_tuple)

Sam1()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_6/pic/Sam1.png)

### Вывод

Пользовательский ввод обрабатывается корректно: строка разделяется по пробелам, преобразуется в целые числа и формируются две коллекции - изменяемый список и неизменяемый кортеж. Задача отражает важность понимания различий между этими структурами данных.

### Задание 2.

Николай знает, что кортежи являются неизменяемыми, но он очень упрямый и всегда хочет доказать, что он прав. Студент решил создать функцию, которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста.

```python
def remove_first_occurrence(tuple_data, element):
    if element not in tuple_data:
        return tuple_data

    lst = list(tuple_data)
    index_to_remove = lst.index(element)
    lst.pop(index_to_remove)
    return tuple(lst)


def Sam2():
    test_cases = [
        ((1, 2, 3), 1),
        ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
        ((2, 4, 6, 6, 4, 2), 9)
    ]

    for tuple_data, element in test_cases:
        result = remove_first_occurrence(tuple_data, element)
        print(f"Входные данные: {tuple_data}, удалить: {element}")
        print(f"Результат: {result}")

Sam2()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_6/pic/Sam2.png)

### Вывод

Для модификации данных пришлось преобразовать кортеж в список, выполнить операцию удаления и вернуть результат обратно в кортеж. Решение эффективно обрабатывает пограничные случаи (отсутствие элемента, одно вхождение), что показывает важность обработки исключительных ситуаций.

### Задание 3.

Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать победителя. Вам им нужно в этом помочь. Дана строка в виде случайной последовательности чисел от 0 до 9 (длина строки минимум 15 символов). Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности.

```python
def build_counts_dict(s):
    counts = {}
    i = 0
    while i < len(s):
        ch = s[i]
        if '0' <= ch <= '9':
            key = ord(ch) - ord('0')
            if key in counts:
                counts[key] = counts[key] + 1
            else:
                counts[key] = 1
        i += 1
    return counts


def top_3_most_frequent(s):
    counts = build_counts_dict(s)
    if not counts:
        return {}

    pairs = []
    for k in counts:
        pairs.append((k, counts[k]))

    top_pairs = []
    temp_pairs = list(pairs)
    take = 3
    while take > 0 and temp_pairs:
        max_idx = 0
        j = 1
        while j < len(temp_pairs):
            # сравним частоты
            if temp_pairs[j][1] > temp_pairs[max_idx][1]:
                max_idx = j
            elif temp_pairs[j][1] == temp_pairs[max_idx][1]:
                if temp_pairs[j][0] < temp_pairs[max_idx][0]:
                    max_idx = j
            j += 1
        top_pairs.append(temp_pairs[max_idx])
        temp_pairs.pop(max_idx)
        take -= 1

    i = 0
    while i < len(top_pairs):
        min_idx = i
        j = i + 1
        while j < len(top_pairs):
            if top_pairs[j][0] < top_pairs[min_idx][0]:
                min_idx = j
            j += 1
        if min_idx != i:
            tmp = top_pairs[i]
            top_pairs[i] = top_pairs[min_idx]
            top_pairs[min_idx] = tmp
        i += 1

    result = {}
    i = 0
    while i < len(top_pairs):
        k, cnt = top_pairs[i]
        result[k] = cnt
        i += 1

    return result

if __name__ == '__main__':
    s = "012345678901234567890123456789012345"
    s2 = "1112233344555599999000000123456789012345"
    counts_all = build_counts_dict(s2)
    top3 = top_3_most_frequent(s2)
    print("Полный словарь частот:", counts_all)
    print("Топ-3 самых частых (словарь):", top3)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_6/pic/Sam3.png)

### Вывод

Алгоритм подсчета частоты цифр демонстрирует применение словарей для статистического анализа. Сортировка по убыванию частоты и возрастанию ключа показывает продвинутые техники работы с коллекциями. Задача имеет практическое применение в анализе данных.

### Задание 4.

Ваш хороший друг владеет офисом со входом по электронным картам, ему нужно чтобы вы написали программу, которая показывала в каком порядке сотрудники входили и выходили из офиса. Определение сотрудника происходит по id. Напишите функцию, которая на вход принимает кортеж и случайный элемент (id), его можно придумать самостоятельно

```python
from typing import Tuple, Any

def slice_first_to_second(tpl: Tuple[Any, ...], x: Any) -> Tuple[Any, ...]:
    try:
        first = tpl.index(x)
    except ValueError:
        return ()
    try:
        second = tpl.index(x, first+1)
    except ValueError:
        return tpl[first:]
    return tpl[first:second+1]

if __name__ == '__main__':
    print(slice_first_to_second((1,2,3), 8))          
    print(slice_first_to_second((1,8,3,4,8,9,2), 8))      
    print(slice_first_to_second((1,2,8,5,1,2,9), 8))  
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_6/pic/Sam4.png)

### Вывод

ешение эффективно обрабатывает три возможных сценария: отсутствие элемента, одно вхождение и multiple вхождения.

### Задание 5.

Самостоятельно придумайте и решите задачу, в которой будут обязательно использоваться кортеж или список. Проведите минимум три теста для проверки работоспособности вашей задачи.

```python
def find_min_max(tuple_data):

    if not tuple_data:
        return "Кортеж пуст"

    return (min(tuple_data), max(tuple_data))


def Sam5():
    test1 = (5, 2, 8, 1, 9, 3)
    print(f"Тест 1: {test1}")
    print(f"Результат: {find_min_max(test1)}")

    test2 = (-5, -2, -8, -1, -9)
    print(f"\nТест 2: {test2}")
    print(f"Результат: {find_min_max(test2)}")

    test3 = (42,)
    print(f"\nТест 3: {test3}")
    print(f"Результат: {find_min_max(test3)}")

Sam5()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_6/pic/Sam5.png)

### Вывод

Тестирование подтверждает корректность работы при различных входных данных.
