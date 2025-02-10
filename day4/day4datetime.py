import pandas as pd

# Создаем DataFrame с датами в виде строк
data = pd.DataFrame({
    'date': ['2023-01-01', '2023-02-15', '2023-03-10'],
    'sales': [200, 150, 300]
})

print("\nDataFrame")
print(data)
print()

# Преобразуем строковые даты в тип datetime
data['date'] = pd.to_datetime(data['date'])
print("Преобразованный DataFrame с датами:")
print(data)
print()

# Извлекаем год, месяц и день
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['day'] = data['date'].dt.day
print("\nDataFrame с добавленными годом, месяцем и днем:")
print(data)
print()

# Фильтрация данных за февраль 2023
february_data = data[data['date'].dt.month == 2]
print("\nДанные за февраль 2023:")
print(february_data)
print()

# Пример группировки по году и месяцу для суммирования продаж
monthly_sales = data.groupby(data['date'].dt.to_period('M'))['sales'].sum()
print("\nСумма продаж по месяцам:")
print(monthly_sales)
print()

# Создаем последовательность дат с 1 января 2023 года по 10 января 2023 года
date_range = pd.date_range(start='2023-01-01', end='2023-01-10')
print("\nСозданная последовательность дат:")
print(date_range)


