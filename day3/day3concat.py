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

# Объединение по строкам
concat_rows = pd.concat([data1, data2], ignore_index=True)
print("\nОбъединение по строкам:")
print(concat_rows)
print()

# Объединение по столбцам (axis=1)
concat_columns = pd.concat([data1, data2], axis=1)
print("\nОбъединение по столбцам:")
print(concat_columns)
print()

#1. ignore_index=True -------------------------------------------------------------------------------
# Создадим два DataFrame с собственными индексами
data1 = pd.DataFrame({
    'product': ['Widget A', 'Widget B'],
    'price': [100, 200]
}, index=[1, 2])

data2 = pd.DataFrame({
    'product': ['Widget C', 'Widget D'],
    'price': [300, 400]
}, index=[3, 4])

# Объединим без ignore_index
concat_data = pd.concat([data1, data2])
print("Без ignore_index:")
print(concat_data)

# Объединим с ignore_index=True
concat_data_ignore_index = pd.concat([data1, data2], ignore_index=True)
print("\nС ignore_index=True:")
print(concat_data_ignore_index)
print()

#2. axis=1----------------------------------------------------------------------------------------------
data1 = pd.DataFrame({
    'product': ['Widget A', 'Widget B'],
    'price': [100, 200]
})

data2 = pd.DataFrame({
    'quantity_sold': [10, 15]
})

# Объединение по строкам (axis=0, по умолчанию)
concat_rows = pd.concat([data1, data2], ignore_index=True)
print("Объединение по строкам (axis=0):")
print(concat_rows)
print()

# Объединение по столбцам (axis=1)
concat_columns = pd.concat([data1, data2], axis=1)
print("\nОбъединение по столбцам (axis=1):")
print(concat_columns)





