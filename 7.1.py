# На вход программа получает имя, фамилию и пароль от 2х пользователей. Пользователь
# может вводить данные в любом порядке. Необхожимо создать кортежей из почты обоих пользователей.

user1 = tuple(input('Введите имя, фамилию, пароль и электронную почту в любом порядке: ').split())
user2 = tuple(input('Введите имя, фамилию, пароль и электронную почту в любом порядке: ').split())
print('Пользователь №1:', user1)
print('Пользователь №2:', user2)

mails = []

for i in user1:
    if '@' in i:
        mails.append(i)
for i in user2:
    if '@' in i:
        mails.append(i)
mails = tuple(mails)
print('Адрес электронной почты:', mails[0])
print('Адрес электронной почты:', mails[1])
# Stan Marsh 1111111 Stan_Marsh@mail.ru
# Eric Cartman 2222222 Eric_Cartman@mail.ru

