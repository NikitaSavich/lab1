text = input("Введите строку: ")
clean_text = text.replace(" ", "").lower()
reversed_text = ""
for char in clean_text:
    reversed_text = char + reversed_text
if clean_text == reversed_text:
    print(f"Строка '{text}' является палиндромом.")
else:
    print(f"Строка '{text}' НЕ является палиндромом.")