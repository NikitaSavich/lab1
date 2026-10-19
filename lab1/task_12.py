def analyze_words(word_list):
    if len(word_list) == 0:
        print("Список слов пуст.")
        return
    print(f"Список слов: {word_list}")
    print(f"Общее количество слов: {len(word_list)}")
    freq = {}
    for w in word_list:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    print(f"Частота каждого слова: {freq}")
    most_frequent_word = word_list[0]
    max_count = 0
    for w, count in freq.items():
        if count > max_count:
            max_count = count
            most_frequent_word = w
    print(f"Самое часто встречающееся слово: '{most_frequent_word}' ({max_count} раз)")
    shortest = word_list[0]
    longest = word_list[0]
    for w in word_list:
        if len(w) < len(shortest):
            shortest = w
        if len(w) > len(longest):
            longest = w
    print(f"Самое короткое слово: '{shortest}'")
    print(f"Самое длинное слово: '{longest}'")
text = input("Введите текст для анализа: ")
for punct in ".,!?;:-()\"'":
    text = text.replace(punct, "")
words = text.lower().split()
print("\nПервичный анализ текста: ")
analyze_words(words)
filtered_words = []
for w in words:
    if len(w) >= 3:
        filtered_words.append(w)
print("\nПовторный анализ (слова от 3 символов): ")
analyze_words(filtered_words)