import csv

# Читаем заголовки обоих файлов
with open('data/turbine_5yr_complex_data.csv', 'r') as f:
    reader = csv.reader(f)
    header1 = next(reader)

with open('data/turbine_5yr_labeled_data.csv', 'r') as f:
    reader = csv.reader(f)
    header2 = next(reader)

print('=== СРАВНЕНИЕ СТРУКТУРЫ ФАЙЛОВ ===\n')
print(f'Файл 1: turbine_5yr_complex_data.csv')
print(f'Количество колонок: {len(header1)}')
print(f'Колонки: {header1}\n')

print(f'Файл 2: turbine_5yr_labeled_data.csv')
print(f'Количество колонок: {len(header2)}')
print(f'Колонки: {header2}\n')

cols1 = set(header1)
cols2 = set(header2)

print('=== ОТЛИЧИЯ ===')
print(f'Только в complex_data: {cols1 - cols2}')
print(f'Только в labeled_data: {cols2 - cols1}')
print(f'Общие колонки: {sorted(cols1 & cols2)}')

# Подсчитаем количество строк
with open('data/turbine_5yr_complex_data.csv', 'r') as f:
    count1 = sum(1 for line in f) - 1  # минус заголовок

with open('data/turbine_5yr_labeled_data.csv', 'r') as f:
    count2 = sum(1 for line in f) - 1  # минус заголовок

print(f'\nКоличество строк в complex_data: {count1}')
print(f'Количество строк в labeled_data: {count2}')

