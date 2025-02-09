#Задача 5: Применение функции с apply()
#1. Создай новый столбец sales_with_tax, где к каждому значению sales будет прибавлен налог 10%.
#2. Напиши функцию, которая будет классифицировать продукты в новый столбец sales_category:
# если sales больше 200, присваивай категорию "High", если меньше или равно 200 — "Low".
# Примените эту функцию с помощью apply().

import pandas as pd

data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget A', 'Widget C', 'Widget B'],
    'region': ['North', 'South', 'East', 'North', 'South'],
    'sales': [200, 300, 150, 400, 100],
    'quantity': [10, 15, 8, 5, 12]
})

#1. Создай новый столбец sales_with_tax, где к каждому значению sales будет прибавлен налог 10%.
# Создаем новый столбец sales_with_tax, добавляя 10% налог к каждому значению продаж
data['sales_with_tax'] = data['sales'].apply(lambda x: x * 1.1)
print("Данные с налогом:")
print(data)
print()

# Функция для присвоения категории 'High' или 'Low' в зависимости от значения sales
def categorize_sales(sales):
    if sales > 200:
        return 'High'
    else:
        return 'Low'

# Применяем функцию к каждому значению sales и сохраняем результат в новый столбец sales_category
data['sales_category'] = data['sales'].apply(categorize_sales)
print("\nДанные с категорией продаж:")
print(data)