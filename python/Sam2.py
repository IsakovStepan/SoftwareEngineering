def read_file_safe(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

            if not content.strip():
                raise ValueError("файл пустой")

            print(f"Содержимое файла '{filename}':")
            print(content)

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")

if __name__ == '__main__':
    with open('empty_file.txt', 'w', encoding='utf-8') as f:
        pass

    with open('data_file.txt', 'w', encoding='utf-8') as f:
        f.write("Это тестовые данные для проверки работы программы.\n")
        f.write("Файл содержит информацию для обработки.\n")

    read_file_safe('empty_file.txt')

    read_file_safe('data_file.txt')

    read_file_safe('nonexistent_file.txt')