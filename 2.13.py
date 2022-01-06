# Вход: слово. Программа проверяет является ли введенное слово палиндром.

enter = str(input('Введите слово или число: '))
word = str(enter.lower())
polind = [str(symbol) for symbol in word]
check = polind[::-1]
print(check)

if polind == check:
    print(True)
else:
    print(False)
