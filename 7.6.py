# Программа на вход получает среднюю температуру за несколько дней.
# Посчитайте среднюю температуру.
temp = []
print('Введите температуру за несколько дней')
a = int(input('>>> '))
temp.append(a)
print('Температура за', len(temp), 'дней:', sum(temp)/len(temp))