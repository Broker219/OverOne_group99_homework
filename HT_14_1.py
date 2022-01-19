# Создать класс Dog.
# Класс имеет четыре атрибута: height, weight, name, age. Класс
# имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.

class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump():
        print('First method')

    def run():
        print('Second method')

    def bark():
        print('Third method')


if __name__ == '__main__':
    dog1 = Dog(50, 30, 'Bobik', 5)
    print(dog1.__dict__)

Dog.jump()
Dog.run()
Dog.bark()
