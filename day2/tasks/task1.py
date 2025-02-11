#Задача 1: Работа с пропущенными значениями
#У тебя есть данные о продуктах, но в них присутствуют пропуски. Загрузите следующий DataFrame и проделай с ним задачи:
#1. Посмотри на данные и выяви, в каких колонках есть пропущенные значения.
#2. Удали строки с пропущенными значениями и выведи результат.
#3. Теперь заполни все пропущенные значения значением 0 и выведи результат.

import pandas as pd

data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget C', 'Widget D', None],
    'sales': [200, None, 300, 150, 100],
    'quantity': [10, None, 15, 7, None]
})

#1. Посмотри на данные и выяви, в каких колонках есть пропущенные значения.
print(data)
print()
#2. Удали строки с пропущенными значениями и выведи результат.
data_no_na = data.dropna()
print(data_no_na)
print()
#3. Теперь заполни все пропущенные значения значением 0 и выведи результат.
data_filled = data.fillna(0)
print(data_filled)