def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args):
            if len(args) != len(expected_types):
                raise TypeError("Количество аргументов не совпадает с количеством проверяемых типов.")
            for i in range(len(args)):
                if type(args[i]) != expected_types[i]:
                    raise TypeError(
                        f"Аргумент {i + 1} должен быть типа {expected_types[i].__name__}, "
                        f"но получен {type(args[i]).__name__}"
                    )
            return func(*args)
        return wrapper
    return decorator
@type_check(int, int)
def add(a, b):
    return a + b
print(f"Результат сложения: {add(10, 20)}")