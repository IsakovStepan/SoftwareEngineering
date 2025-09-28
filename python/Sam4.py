a = input("Введите предложение: ")

print("Длина предложения:", len(a))
print("Предложение в нижнем регистре:", a.lower())
print("Количество гласных:", sum(i in "aeiou" for i in a.lower()))
print("Замена ugly на beauty:", a.replace("ugly", "beauty"))
print("Начинается на The:", a.startswith("The"))
print("Заканчивается на end:", a.endswith("end"))