list1 = [float(x) if "." in x else int(x) for x in input("Введите 1-й набор чисел через пробел: ").split()]
list2 = [float(x) if "." in x else int(x) for x in input("Введите 2-й набор чисел через пробел: ").split()]
common = []
for x in list1:
    if x in list2 and x not in common:
        common.append(x)
only_in_first = []
for x in list1:
    if x not in list2 and x not in only_in_first:
        only_in_first.append(x)
only_in_second = []
for x in list2:
    if x not in list1 and x not in only_in_second:
        only_in_second.append(x)
symmetric_diff = only_in_first + only_in_second
print(f"1. Присутствуют в обоих наборах: {common}")
print(f"2. Только в первом наборе: {only_in_first}; только во втором: {only_in_second}")
print(f"3. Числа из обоих наборов без общих: {symmetric_diff}")