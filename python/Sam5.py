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