def cache(func):
    saved_results = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in saved_results:
            print(f"[Из кэша] Для аргументов {args}:")
            return saved_results[key]
        result = func(*args, **kwargs)
        saved_results[key] = result
        return result
    return wrapper
@cache
def multiply(a, b):
    print("Выполняется вычисление...")
    return a * b
print(multiply(4, 5))
print(multiply(4, 5))