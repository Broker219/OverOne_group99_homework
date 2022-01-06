# Вход: 2 строки. Программа проверяет входит ли одна строка во вторую. Если да, то выводит
# “I’m here’, если нет, то “I’m not here’

str1 = str(input('Введите строку: '))
str2 = str(input('Введите вторую строку: '))

if str2 in str1 or str1 in str2:
    print('I’m here')
else:
    print('I’m not here')
