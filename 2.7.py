# Создать переменную 'program'. Программа должна выводить все индыксы буквы 'r'

print('Программа найдет индекс указанных букв, в веденных словах')

random_word = str(input('Введите слово: '))
word = str(random_word.lower())

random_letter = str(input('Какую букву нужно найти? '))
letter = str(random_letter.lower())

positions = [i for i, c in enumerate(word) if c == letter]
print('Индекс буквы', letter, 'в слове', word, '=', positions)
