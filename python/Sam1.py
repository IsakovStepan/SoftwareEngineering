def Sam1():
    data = input("Введите числа через пробел: ")

    numbers_list = [int(x) for x in data.split()]
    numbers_tuple = tuple(numbers_list)

    print("Список:", numbers_list)
    print("Кортеж:", numbers_tuple)

Sam1()