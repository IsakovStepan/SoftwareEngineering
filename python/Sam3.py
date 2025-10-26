def analyze_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    letters = sum(1 for char in text if char.isalpha())

    words = len(text.split())

    lines = text.count('\n') + 1 if text else 0

    print(f" {letters} letters")
    print(f" {words} words")
    print(f" {lines} lines")

analyze_file("input.txt")