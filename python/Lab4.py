numbers = [1, 3, 4, 5, 8, 9, 15, 16, 73, 321, 322]
value =  int(input('Введите значение переменной: '))
if value in numbers:
    if value % 2 == 0:
        print('Переменная чётная и есть в массиве')
    else:
        print('Переменная нечётная и есть в массиве')
else:
    print(f"Переменной нет в массиве numbers и она равна {value}")