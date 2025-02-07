import pandas as pd

# Создание DataFrame для группировки
data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget A', 'Widget C'],
    'region': ['North', 'South', 'North', 'South'],
    'sales': [200, 300, 150, 400]
})

# Группировка по продукту с суммированием продаж
grouped_data = data.groupby('product')['sales'].sum()
print("\nСумма продаж по продукту:")
print(grouped_data)

grouped_region = data.groupby('region')['sales'].sum()
print("\nСумма продаж по региону:")
print(grouped_region)

