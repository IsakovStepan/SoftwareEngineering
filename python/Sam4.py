def average(*args):
    return sum(args) / len(args) if args else 0

if __name__ == '__main__':
    print(average(10, 20, 30, 40))
    print(average(5))
    print(average())