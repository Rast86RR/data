import pandas as pd



# Загрузка данных из CSV
data = pd.read_csv('sales_data.csv')  # Замените 'sales_data.csv' на путь к вашему файлу

# Просмотр первых строк
print(data.head())

# Описание данных
print(data.describe())

# Фильтрация данных (например, выбрать только продажи в определенном регионе)
filtered_data = data[data['region'] == 'North']

# Группировка данных по колонке 'product' и суммирование по 'sales'
grouped_data = data.groupby('product')['sales'].sum()

print(grouped_data)
