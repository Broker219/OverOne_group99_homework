# Напишите функцию, которая будет принимать номер
# кредитной карты и показывать только последние 4 цифры.
# Остальные цифры должны заменяться звездочками
# 5456789515658562
# >> ************8562


# def remake(remake):
#     end_nums = remake[-1:-4]
#     return '*' * (int(len(remake) - 4)) + remake[-4] + remake[-3] + remake[-2] + remake[-1]
#
#
# print(remake(str(input('Номер карты: '))))


# Напишите функцию, которая проверяет: является ли слово палиндромом


# def is_palindrome(palindrome):
#     if palindrome == palindrome[::-1]:
#         print(True)
#     else:
#         print(False)
#     return
#
#
# print(is_palindrome(str(input('Введите слово: '))))

# Напишите классы Круг, Прямоугольник, Квадрат.
# Каждый класс должен содержать метод нахождения площади фигуры.
# Используйте :
# - Наследование
# - Абстрактный класс и методы
# - Округлите площадь круга до 2х чисел после запятой
# - Число π возьмите из модуля math
# square = Square(4)
# rectangle = Rectangle(2,6)
# circle = Circle(3)
# figures =[square, rectangle, circle]
# for i in figures:
# print(i.area())
# >> Площадь квадрата = 16
# Площаль прямоугольника = 12
# Площадь круга равна = 28.27

import math


class Circle:
    # S = d2 : 4 × π
    def s_circle(circle):
        s_circle = circle ** 2 / 4 * math.pi
        return s_circle


class Rectangle:
    def s_rectangle(rectangle):
        s_rectangle = 1 * rectangle[0] * rectangle[1]
        return s_rectangle


class Square:
    def s_square(square):
        s_square = square ** 2
        return s_square


Circle.circle = int(input('Введите диаметр круга: '))
Rectangle.rectangle = [int(i) for i in input('Введите длину двух сторон прямоугольника: ').split()]
Square.square = int(input('Введите длину одной стороны квадрата: '))

# Что то я не доделал, я не понял что

print('Площадь круга равна:', Circle.s_circle)
print('Площадь прямогугольника равна:', Rectangle.s_rectangle)
print('Площадь квадрата равна:', Square.s_square)

