import pandas as pd

# Создание DataFrame с пропущенными значениями
data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget C', None],
    'sales': [200, None, 300, 150],
    'quantity': [10, 15, None, 7]
})

# Фильтрация строк, где продажи больше 200
high_sales = data[data['sales'] > 200]
print("\nПродажи больше 200:")
print(high_sales)
