import pandas as pd

# Создание DataFrame с пропущенными значениями
data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget C', None],
    'sales': [200, None, 300, 150],
    'quantity': [10, 15, None, 7]
})

# Сортировка данных по количеству (quantity) в порядке убывания
sorted_data = data.sort_values(by='quantity', ascending=False)
print("\nСортировка по количеству в порядке убывания:")
print(sorted_data)
