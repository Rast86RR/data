#Задача 3: Сортировка данных
#1. Отсортируй строки по колонке sales в порядке возрастания и выведи результат.
#2. Теперь отсортируй строки по quantity в порядке убывания и выведи результат.

import pandas as pd

data = pd.DataFrame({
    'product': ['Widget A', 'Widget B', 'Widget C', 'Widget D', None],
    'sales': [200, None, 300, 150, 100],
    'quantity': [10, None, 15, 7, None]
})

#1. Отсортируй строки по колонке sales в порядке возрастания и выведи результат.
sorted_by_sales = data.sort_values(by = 'sales', ascending=True)
print(sorted_by_sales)
print()
#2. Теперь отсортируй строки по quantity в порядке убывания и выведи результат.
sorted_by_quantity = data.sort_values(by = 'quantity', ascending=False)
print(sorted_by_quantity)