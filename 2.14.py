# Вход: электронная почта. Программа удаляет символ @ из почты.

mail = str(input('Введите адрес электронной почты: '))
symbol = mail.replace('@', ' ')
l_word = str(symbol.lower())
c_word = str(l_word.capitalize())


print('Адрес вашей электронной почты: ' + c_word + ' ' + 'GMail.com')
