def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = 200
fib_gen = fib(n)

with open("fib.txt", "w", encoding="utf-8") as file:
    for i, num in enumerate(fib_gen, 1):
        file.write(f"Число Фибоначчи #{i}: {num}\n")

print(f"Все {n} чисел Фибоначчи записаны в файл 'fib.txt'")

fib_gen = fib(n)
for _ in range(n):
    result = next(fib_gen)
print(f"Число Фибоначчи под номером {n}: {result}")