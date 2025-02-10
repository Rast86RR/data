import pandas as pd

# Первый DataFrame с информацией о продуктах
data1 = pd.DataFrame({
    'product_id': [1, 2, 3],
    'product_name': ['Widget A', 'Widget B', 'Widget C'],
    'price': [100, 200, 300]
})

# Второй DataFrame с информацией о продажах
data2 = pd.DataFrame({
    'product_id': [1, 2, 4],
    'quantity_sold': [10, 20, 15]
})

print("DataFrame 1:")
print(data1)
print()

print("\nDataFrame 2:")
print(data2)
print()

# Установим product_id как индекс
data1.set_index('product_id', inplace=True)
data2.set_index('product_id', inplace=True)

# Выполним соединение join
joined_data = data1.join(data2, how='inner')
print("\nСоединение с использованием join:")
print(joined_data)
