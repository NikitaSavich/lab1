from random import randint
secret_number = randint(1, 100)
print("Угадайте число от 1 до 100")
while True:
    guess = int(input("Ваша догадка: "))
    if guess < secret_number:
        print("Больше")
    elif guess > secret_number:
        print("Меньше")
    else:
        print(f"Поздравляем! Вы угадали число {secret_number}!")
        break