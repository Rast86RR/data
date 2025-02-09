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

# Внутреннее объединение по product_id
merged_inner = data1.merge(data2, on='product_id', how='inner')
print("\nВнутреннее объединение (inner join):")
print(merged_inner)
print()

# Левое объединение (left join)
merged_left = data1.merge(data2, on='product_id', how='left')
print("\nЛевое объединение (left join):")
print(merged_left)
print()

# Правое объединение (right join)
merged_right = data1.merge(data2, on='product_id', how='right')
print("\nПравое объединение (right join):")
print(merged_right)
print()

# Полное объединение (outer join)
merged_outer = data1.merge(data2, on='product_id', how='outer')
print("\nПолное объединение (outer join):")
print(merged_outer)


