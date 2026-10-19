from time import time
def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        elapsed_ms = (end_time - start_time) * 1000
        print(f"Время выполнения функции '{func.__name__}': {elapsed_ms:.3f} мс")
        return result
    return wrapper
@timing
def calculate_squares(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total
calculate_squares(100000)