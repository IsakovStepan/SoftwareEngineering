from Heron import heron

if __name__ == '__main__':
    a = float(input("Введите длину первой стороны: "))
    b = float(input("Введите длину второй стороны: "))
    c = float(input("Введите длину третьей стороны: "))
    area = heron(a, b, c)
    print(f"Площадь треугольника: {area:.2f}")