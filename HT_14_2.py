# Добавить в класс Dog метод change_name.
# Метод принимает на вход новое имя и меняет  атрибут имени у объекта.
# Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.


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

    def change_name(name=input('Please, enter the name: ')):
        if len(name) > 1:
            return name


if __name__ == '__main__':
    dog1 = Dog(50, 30, Dog.change_name(), 5)
    print(dog1.__dict__)

Dog.jump()
Dog.run()
Dog.bark()