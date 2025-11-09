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