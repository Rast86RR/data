import pandas as pd

# Укажи полный путь к файлу
file_path = "/Users/rastsislaurudziankou/Documents/my/data/csv/sales_data.csv"

# Загрузка данных из CSV
data = pd.read_csv(file_path)

# Просмотр первых строк
#print(data.head())

# Описание данных
#print(data.describe())

# Фильтрация данных (например, выбрать только продажи в определенном регионе)
#filtered_data = data[data['region'] == 'North']
#print(filtered_data)

# Группировка данных по колонке 'product' и суммирование по 'sales'
grouped_data = data.groupby('product')['sales'].sum()
print(grouped_data)
