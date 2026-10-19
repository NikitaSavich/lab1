raw_input = input("Введите числа через пробел: ").split()
numbers = []
for item in raw_input:
    if "." in item:
        numbers.append(float(item))
    else:
        numbers.append(int(item))
unique_nums = []
repeated_nums = []
for n in numbers:
    if n not in unique_nums:
        unique_nums.append(n)
    else:
        if n not in repeated_nums:
            repeated_nums.append(n)
even_nums = []
odd_nums = []
for n in numbers:
    if type(n) == int:
        if n % 2 == 0:
            even_nums.append(n)
        else:
            odd_nums.append(n)
negative_nums = []
for n in numbers:
    if n < 0:
        negative_nums.append(n)
float_nums = []
for n in numbers:
    if type(n) == float:
        float_nums.append(n)
sum_mult_5 = 0
for n in numbers:
    if n % 5 == 0:
        sum_mult_5 += n
max_num = numbers[0]
min_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n
print(f"1. Список без дубликатов (уникальные значения): {unique_nums}")
print(f"2. Повторяющиеся числа: {repeated_nums}")
print(f"3. Четные числа: {even_nums}, Нечетные числа: {odd_nums}")
print(f"4. Отрицательные числа: {negative_nums}")
print(f"5. Числа с плавающей точкой: {float_nums}")
print(f"6. Сумма чисел, кратных 5: {sum_mult_5}")
print(f"7. Самое большое число: {max_num}")
print(f"8. Самое маленькое число: {min_num}")