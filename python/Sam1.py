def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = 200
fib_gen = fib(n)
result = None
for _ in range(n):
    result = next(fib_gen)

print(f"Число Фибоначчи под номером {n}: {result}")