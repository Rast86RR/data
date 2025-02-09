#Задача 2: Фильтрация данных
#1. Из исходных данных выбери только строки, где sales больше или равен 150.
#2. Отфильтруй строки, где продукт (product) не равен "Widget A".

import pandas as pd

data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget C', 'Widget D', None],
    'sales': [200, None, 300, 150, 100],
    'quantity': [10, None, 15, 7, None]
})

#1. Из исходных данных выбери только строки, где sales больше или равен 150.
data_sale_more_150 = data[data['sales'] > 150]
print(data_sale_more_150)
print()
#2. Отфильтруй строки, где продукт (product) не равен "Widget A".
data_without_WA = data[data['product'] != 'Widget A']
print(data_without_WA)