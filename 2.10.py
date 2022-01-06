# Создать переменные. Программа меняет дни местами

print('____________Первый вариант____________')
a = 'Today is Monday'
b = 'Tomorrow is Friday'

print(a.replace('Monday', 'Friday'))
print(b.replace('Friday', 'Monday'))

print('____________Второй вариант____________')

x = a.replace(a[9:], b[12:])
y = b.replace(b[12:], a[9:])

print(x)
print(y)
print('_____________________________________')