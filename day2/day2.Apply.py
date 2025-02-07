import pandas as pd

# Создание DataFrame для группировки
data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget A', 'Widget C'],
    'region': ['North', 'South', 'North', 'South'],
    'sales': [200, 300, 150, 400]
})

# Применение функции для пересчета продаж с налогом 10%
data['sales_with_tax'] = data['sales'].apply(lambda x: x * 1.10)
print("\nПродажи с налогом:")
print(data)
