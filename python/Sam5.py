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