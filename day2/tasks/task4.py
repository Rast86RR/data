#Задача 4: Группировка и агрегирование
#1. Группируй данные по product и найди общую сумму sales для каждого продукта.
#2. Группируй данные по region и посчитай среднее значение quantity для каждого региона.

import pandas as pd

data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget A', 'Widget C', 'Widget B'],
    'region': ['North', 'South', 'East', 'North', 'South'],
    'sales': [200, 300, 150, 400, 100],
    'quantity': [10, 15, 8, 5, 12]
})

#1. Группируй данные по product и найди общую сумму sales для каждого продукта.
group_by_product = data.groupby('product')['sales'].sum()
print(group_by_product)
print()
#2. Группируй данные по region и посчитай среднее значение quantity для каждого региона.
group_by_region = data.groupby('region')['quantity'].mean()
print(group_by_region)