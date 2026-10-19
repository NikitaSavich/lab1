from datetime import datetime
def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"[{now}] Вызов {func.__name__} с args={args}, kwargs={kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator
@log_calls("calls.log")
def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"
print(greet("Алексей"))
print(greet("Мария", greeting="Здравствуйте"))