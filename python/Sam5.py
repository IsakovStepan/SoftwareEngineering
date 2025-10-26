def word_statistics():
    filename = input("Введите имя файла: ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        words = text.split()

        total_words = len(words)
        total_chars = sum(len(word) for word in words)
        avg_word_length = total_chars / total_words if total_words > 0 else 0

        longest_word = max(words, key=len) if words else ""

        print(f"\nСтатистика файла '{filename}':")
        print(f"Количество слов: {total_words}")
        print(f"Общее количество символов: {total_chars}")
        print(f"Средняя длина слова: {avg_word_length:.1f}")
        print(f"Самое длинное слово: '{longest_word}'")

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")


word_statistics()