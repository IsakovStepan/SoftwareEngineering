class NegativeNumberError(Exception):
    def __init__(self, value, message="Отрицательные числа не допускаются"):
        self.value = value
        self.message = f"{message}: получено {value}"
        super().__init__(self.message)


def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError(number, "Невозможно вычислить квадратный корень")

    result = number ** 0.5
    print(f"Квадратный корень из {number} равен {result:.2f}")
    return result


def process_age(age):
    if age < 0:
        raise NegativeNumberError(age, "Возраст не может быть отрицательным")

    print(f"Возраст {age} лет корректен")
    return age

if __name__ == '__main__':
    try:
        calculate_square_root(16)
        process_age(25)
    except NegativeNumberError as e:
        print(f"Поймано исключение: {e}")

    try:
        calculate_square_root(-4)
    except NegativeNumberError as e:
        print(f"Поймано исключение: {e}")

    try:
        process_age(-5)
    except NegativeNumberError as e:
        print(f"Поймано исключение: {e}")

    try:
        calculate_square_root(9)
        process_age(-10)
        calculate_square_root(25)
    except NegativeNumberError as e:
        print(f"Поймано исключение: {e}")