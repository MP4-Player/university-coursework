def find_common_words(sentence1, sentence2):
  words1 = sentence1.lower().split()
  words2 = sentence2.lower().split()
  common_words = []

  # Проходим по каждому слову из первого предложения
  for word1 in words1:
    # Проверяем, есть ли слово в словах второго предложения
    for word2 in words2:
      if word1 == word2:
        # Если слово есть, добавляем его в список общих слов
        if word1 not in common_words:  # Проверяем на дубликаты
          common_words.append(word1)
        break  # Переходим к следующему слову из первого предложения

  return common_words

# Задаем предложения
sentence1 = "apple apple sik dofomin fin g"
sentence2 = "apple sat dezomorfin f  g h j "

# Находим общие слова
common_words = find_common_words(sentence1, sentence2)

# Выводим результат
print("Общие слова в предложениях:")
print(", ".join(common_words))
