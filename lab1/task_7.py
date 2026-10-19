minutes = int(input("Введите количество израсходованных минут: "))
sms = int(input("Введите количество израсходованных СМС: "))
mb = float(input("Введите количество израсходованного интернет-трафика (в МБ): "))
base_price = 24.99
extra_minutes_cost = 0.0
extra_sms_cost = 0.0
extra_mb_cost = 0.0
if minutes > 60:
    extra_minutes_cost = (minutes - 60) * 0.89
if sms > 30:
    extra_sms_cost = (sms - 30) * 0.59
if mb > 1024:
    extra_mb_cost = (mb - 1024) * 0.79
subtotal = base_price + extra_minutes_cost + extra_sms_cost + extra_mb_cost
tax = subtotal * 0.02
total = subtotal + tax
print(f"Базовая сумма тарификации: {base_price:.2f} руб.")
if extra_minutes_cost > 0:
    print(f"Дополнительные минуты: {extra_minutes_cost:.2f} руб.")
if extra_sms_cost > 0:
    print(f"Дополнительные СМС-сообщения: {extra_sms_cost:.2f} руб.")
if extra_mb_cost > 0:
    print(f"Дополнительный интернет-трафик: {extra_mb_cost:.2f} руб.")
print(f"Налог (2%): {tax:.2f} руб.")
print(f"Итоговая сумма к оплате: {total:.2f} руб.")