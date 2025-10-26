from collections import Counter

with open("article.txt", encoding="utf-8") as f:
    text = f.read().lower().split()

word_count = len(text)
most_common = Counter(text).most_common(1)[0]

print(f"Количество слов: {word_count}")
print(f"Самое частое слово: '{most_common[0]}'")
print(f"Количество повторений встречается: {most_common[1]} раз(а)")