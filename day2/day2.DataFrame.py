import pandas as pd

# Создание DataFrame с пропущенными значениями
data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget C', None],
    'sales': [200, None, 300, 150],
    'quantity': [10, 15, None, 7]
})

print("Исходные данные с пропущенными значениями:")
print(data)

# Удалить строки с пропусками
data_no_na = data.dropna()
print("\nДанные без пропусков:")
print(data_no_na)

# Заполнить пропуски значением
data_filled = data.fillna(0)
print("\nДанные с заполненными пропусками:")
print(data_filled)
