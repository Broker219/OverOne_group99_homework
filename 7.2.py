# Анна регистрируется на сайте. Ей надо ввести имя,
# фамилию, возраст и пароль. Она ввела только «Anna» и
# почту. Необходимо создать кортеж из имени и почты.

print('Введите имя и фамилию: ')
print('Введите свой возраст: ')
print('Создайте пароль: ')

enter = tuple(input('>>> ').split())
data = []

for i in enter:
      data.append(i)
data = tuple(data)
print('Проверьте ваши данные:', data)

# Anna Anna_Sitis@mail.com
