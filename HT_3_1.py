# Вход: разные слова. Программа создает из них список и выводит его задом наперед.

word1 = input('Please, enter first words : ')
word2 = input('Please, enter second words : ')
word3 = input('Please, enter third words : ')
word4 = input('Please, enter four words : ')
ls = [word1, word2, word3, word4]
print(ls)
ls.reverse()
print(ls)
