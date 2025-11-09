# Тема 9. Концепции и принципы ООП
Отчет по Теме №8 выполнил:
- Исаков Степан Юрьевич
- ИВТ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + |  |
| Задание 3 | + |  |
| Задание 4 | + |  |
| Задание 5 | + |  |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

---

## Лабораторная работа №9
### Задание 1.

Создайте класс, указав в свойствах только имя. Дальше создайте функцию __init__(), а в ней сделайте проверку на то угадал человек ваше имя или нет.

```python
class Ivan:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Иван':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Иван"

person1 = Ivan('Алексей')
person2 = Ivan('Иван')
print(person1.name)
print(person2.name)

person2.surname = 'Петров'
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_9/pic/Lab1.png)

### Вывод

Продемонстрировано ограничение атрибутов класса с помощью __slots__.

### Задание 2.

Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения.

```python
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженное с {self.ingredient}")
        else:
            print("Обычное мороженое")

icecream = Icecream()
icecream.composition()
icecream = Icecream('шоколадом')
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_9/pic/Lab2.png)

### Вывод

Реализована проверка типа топпинга через isinstance().

### Задание 3.

Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_9/pic/Lab3.png)

### Вывод

Созданы property-методы для контролируемого доступа к защищенным атрибутам.

### Задание 4.

Нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи Михаил А. Панов “наследования” объяснить компьютеру что кошки и собаки – это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга.

```python
class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds}")
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_9/pic/Lab4.png)

### Вывод

Построена иерархия классов млекопитающее-кошка-собака.

### Задание 5.

Программа с полиморфизмом, которая будет описывать всю суть первого предложения задачи. Для этого мы можем выбрать два языка, например, русский и английский.

```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")

class English:
    @staticmethod
    def greeting():
        print("Hello")

def greet(language):
    language.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_9/pic/Lab5.png)

### Вывод

Реализовано полиморфное поведение через статические методы, позволяющее объектам разных классов иметь одинаковый интерфейс.

---

## Самостоятельная работа №9
### Задание 1.

Садовники и помидоры.

```python
class Tomato:
    states = {
        0: 'отсутствует',
        1: 'цветение',
        2: 'зеленый',
        3: 'красный'
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f"Томат {self._index} теперь на стадии: {Tomato.states[self._state]}")

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"{self.name} ухаживает за растением...")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Урожай собран!")
            self._plant.give_away_all()
            return True
        else:
            print("Еще не все томаты созрели! Продолжайте ухаживать за ними.")
            return False

    @staticmethod
    def knowledge_base():
        print("Стадии созревания томата:")
        for key, value in Tomato.states.items():
            print(f"  {key}: {value}")


if __name__ == "__main__":

    Gardener.knowledge_base()


    bush = TomatoBush(3)  # куст с 3 томатами
    gardener = Gardener("Иван", bush)

    print(f"Садовник {gardener.name} начинает работу с {len(bush.tomatoes)} томатами")

    print("\nПервый уход")
    gardener.work()

    print("\nПопытка сбора урожая 1")
    gardener.harvest()

    print("\nВторой уход")
    gardener.work()

    print("\nТретий уход")
    gardener.work()

    print("\nФинальная попытка сбора урожая")
    if gardener.harvest():
        print(f"После сбора урожая осталось томатов: {len(bush.tomatoes)}")
    else:
        print("Что-то пошло не так, урожай не собран")
```

### Результат

![Меню](https://github.com/IsakovStepan/SoftwareEngineering/blob/Tema_9/pic/Sam1.png)

### Вывод

В ходе выполнения самостоятельной работы была успешно программа, моделирующая процесс выращивания томатов садовником.
