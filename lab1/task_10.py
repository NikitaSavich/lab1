amount = float(input("Введите сумму покупки (руб.): "))
age = int(input("Введите возраст покупателя: "))
is_birthday = input("Сегодня День рождения покупателя? (да/нет): ").lower() == "да"
is_vip = input("Клиент имеет статус VIP? (да/нет): ").lower() == "да"
base_discount = 10 if amount > 1000 else 0
if is_vip:
    if 15 > base_discount:
        discount = 15
    else:
        discount = base_discount
else:
    discount = base_discount
if age >= 63:
    discount += 5
if is_birthday:
    discount += 5
if discount > 25:
    discount = 25
final_amount = amount * (1 - discount / 100)
print(f"Итоговая скидка: {discount}%")
print(f"Сумма к оплате со скидкой: {final_amount:.2f} руб.")