# Создать переменные 1 и 123.
# Программа должна проверять вхождение одной переменной в другую.

a = str(input('Введите число: '))
b = str(input('Введите цифру: '))

c = bool(b in a)
if c is True:
    print('Вхождение одной переменной в другую: Истинно')
elif c is False:
    print('Вхождение одной переменной в другую: Ложно')
