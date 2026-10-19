summ = int(input('Введите сумму: '))
denominations = [100, 50, 10, 5, 2, 1]
print('Потребуется: ')
for coin in denominations:
    count = summ // coin
    summ %= coin
    if count > 0:
        label = 'купюр(ы)' if coin >= 5 else 'монеты'
        print(f'- {count} {label} по {coin} рублей')