import functools

class CallCounter:
    def __init__(self, func):
        self.func = func
        self.call_count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"Функция '{self.func.__name__}' вызвана {self.call_count} раз")
        return self.func(*args, **kwargs)


@CallCounter
def calculate_square(n):
    result = n ** 2
    print(f"Квадрат числа {n} равен {result}")
    return result


@CallCounter
def calculate_cube(n):
    result = n ** 3
    print(f"Куб числа {n} равен {result}")
    return result

if __name__ == '__main__':
    calculate_square(5)
    calculate_cube(3)
    calculate_square(10)
    calculate_cube(2)
    calculate_square(7)

    print(f"\nИтоговое количество вызовов:")
    print(f"calculate_square: {calculate_square.call_count}")
    print(f"calculate_cube: {calculate_cube.call_count}")