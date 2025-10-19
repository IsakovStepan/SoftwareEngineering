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