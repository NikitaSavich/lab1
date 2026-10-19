sales = [
    {"name": "Ноутбук", "price": 50000, "quantity": 3},
    {"name": "Мышь", "price": 1500, "quantity": 10},
    {"name": "Ноутбук", "price": 50000, "quantity": 2},
    {"name": "Клавиатура", "price": 3000, "quantity": 5},
    {"name": "Монитор", "price": 20000, "quantity": 4}
]
revenue_by_item = {}
for record in sales:
    name = record["name"]
    revenue = record["price"] * record["quantity"]
    if name in revenue_by_item:
        revenue_by_item[name] += revenue
    else:
        revenue_by_item[name] = revenue
print("Общая выручка по каждому товару:")
for name, rev in revenue_by_item.items():
    print(f" - {name}: {rev} руб.")
most_profitable_name = ""
max_revenue = -1
for name, rev in revenue_by_item.items():
    if rev > max_revenue:
        max_revenue = rev
        most_profitable_name = name
print(f"Самый прибыльный товар: {most_profitable_name} ({max_revenue} руб.)")
print(f"Количество уникальных наименований: {len(revenue_by_item)}")