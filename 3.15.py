# Создать 2 списка:
# 1. [30, 28, 26, 24, 22, 20, 18, 16, 14]
# 2. Из первого списка сделать
# список [14, 16, 18]

ls = [30, 28, 26, 24, 22, 20, 18, 16, 14]
print(ls)
ls.reverse()
print(ls)
del ls[3:]
print(ls)