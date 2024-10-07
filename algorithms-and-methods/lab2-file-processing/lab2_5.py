import re
from collections import Counter

def count_unique_words(file_path):
    unique_words = set()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            unique_words.update(words)

    return len(unique_words)

def count_word_repetitions(file_path):
    word_counts = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            word_counts.update(words)

    return word_counts

file_path = 'lab2_5.txt'

unique_word_count = count_unique_words(file_path)
print(f"Количество уникальных слов: {unique_word_count}")

word_repetitions = count_word_repetitions(file_path)
for word, count in word_repetitions.items():
    print(f"Слово '{word}' встречается {count} раз(а)")