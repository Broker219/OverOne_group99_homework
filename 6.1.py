# По введенному числу N, распечатайте все квадраты чисел до N

n = int(input('Введите число: '))
a = 1

while a <= n:
    print(a * a)
    a += 1
