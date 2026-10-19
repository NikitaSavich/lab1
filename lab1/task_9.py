print("Доступные типы измерений:")
print("1. Длина (мм, см, м, км, дюйм)")
print("2. Масса (мг, г, кг, т)")
print("3. Время (сек, мин, час)")
measure_type = input("Введите номер типа измерения (1, 2 или 3): ")
from_unit = input("Введите исходную единицу: ").lower()
to_unit = input("Введите нужную единицу: ").lower()
value = float(input("Введите значение: "))
rates = {
    "мм": 0.001, "см": 0.01, "м": 1.0, "км": 1000.0, "дюйм": 0.0254,
    "мг": 0.001, "г": 1.0, "кг": 1000.0, "т": 1000000.0,
    "сек": 1.0, "мин": 60.0, "час": 3600.0
}
if from_unit in rates and to_unit in rates:
    base_value = value * rates[from_unit]
    result = base_value / rates[to_unit]
    print(f"Результат: {value} {from_unit} = {result:.4f} {to_unit}")
else:
    print("Ошибка: указаны неизвестные единицы измерения.")