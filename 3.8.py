# Вход: список ['dog', 'cat', 'rat', 'rabbit'].
# Программа делает из него список ['rat', 'rabbit', 'pig', 'dog', 'cat']

ls = ['dog', 'cat', 'rat', 'rabbit']
print(ls)

ls.insert(2, 'pig')
print(ls)

ls.sort()
ls = ls[::-1]
print(ls)
