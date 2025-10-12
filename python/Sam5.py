def transform_set(lst):
    result = set()
    for num in set(lst):
        count = lst.count(num)
        for i in range(1, count + 1):
            if i == 1:
                result.add(num)
            else:
                result.add(str(num) * i)
    return result

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(transform_set(list_1))
print(transform_set(list_2))
print(transform_set(list_3))