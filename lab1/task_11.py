age = int(input("Возраст заемщика: "))
income = float(input("Ежемесячный доход (руб.): "))
loan_amount = float(input("Размер запрашиваемого кредита (руб.): "))
months = int(input("Срок кредита (месяцы): "))
history = input("Кредитная история (отличная/хорошая/удовлетворительная/плохая): ").lower()
has_guarantor = input("Наличие поручителей (да/нет): ").lower() == "да"
has_collateral = input("Наличие залога (да/нет): ").lower() == "да"
monthly_payment = loan_amount / months
dti_ratio = (monthly_payment / income) * 100
score = 0
if 21 <= age <= 65:
    score += 20
else:
    score -= 10
if dti_ratio <= 30:
    score += 30
elif dti_ratio <= 50:
    score += 15
else:
    score -= 20
if history == "отличная":
    score += 30
elif history == "хорошая":
    score += 20
elif history == "удовлетворительная":
    score += 5
else:
    score -= 40
if has_guarantor:
    score += 10
if has_collateral:
    score += 15
if score >= 60:
    risk = "низкий"
    rate = 12.0
    recommendation = "Одобрить кредит на стандартных условиях."
elif score >= 35:
    risk = "средний"
    rate = 16.5
    recommendation = "Одобрить кредит с повышенной ставкой."
elif score >= 10:
    risk = "высокий"
    rate = 22.0
    recommendation = "Требуется дополнительная проверка или уменьшение суммы."
else:
    risk = "критический"
    rate = 0.0
    recommendation = "Отклонить заявку на кредит."
print("\nРезультаты оценки: ")
print(f"Соотношение ежемесячного платежа к доходу: {dti_ratio:.1f}%")
print(f"Категория риска: {risk}")
if rate > 0:
    print(f"Предлагаемая процентная ставка: {rate}% годовых")
else:
    print("Предлагаемая процентная ставка: не применимо (отказ)")
print(f"Рекомендация: {recommendation}")