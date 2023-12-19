"""Домашняя работа - ООП Классы и Объекты
1. Создайте класс Animal.
Где в качестве атрибута принимаются параметры:
- type_animal
- sound
также есть метод makeNoice( ), где при вызове этого метода определенное животное издает свой звук.
Создайте 4 экземпляра объекта Animal для:
- Собаки
- Кошки
- Коровы
- Утки
Пример:
dog = Dog()
dog.makeNoice( )
Результат вызова программы:
Гав Гав!"""
class Animal:
    def __init__(self, type_animal, sound):
        self.name_animal = type_animal
        self.sound = sound
    def makeNoice(self):
        print(f'Result of program....\n{self.name_animal}\n{self.sound}')
dogs = Animal('Dog','Gav Gav!')
cats = Animal('Cat', 'Miu Miu!')
cows = Animal('Cow','Muu Muu!')
dugs = Animal('Dug','Krya Krya!')
# cats.makeNoice()

"""2. Создайте класс Vehicle, где в качестве атрибута принимаются
следующие переменные в конструктор – brandCar, nameCar,
maxSpeed, color
Создайте следующие методы:
• Метод, который отображает все информации о том или
ином автомобиле
• Метод, возвращает тип автомобиля в зависимости от
скорости автомобиля при следующих условиях:
- Метод должен возвращать «Семейный», если
максимальная скорость не достигает 150 км/ч.
- Метод возвращает «Школьный», если скорость
не достигает 80 км/ч
- Метод возвращает «Спортивный», если скорость
автомобиля превышает 150 км/ч
• Метод при вызове, которой меняет цвет автомобиля"""
class Vehicle():
    def __init__(self, brandCar, nameCar, maxSpeed, color):
        self.brand = brandCar
        self.name = nameCar
        self.speed = int(maxSpeed)
        self.color = color
    def display_info(self):
        print(f'Brand car: {self.brand}\nName of car: {self.name}\nSpeed car: {self.speed}\nColor car: {self.color}\n')
    def type_car(self):
        if 80 <= self.speed < 150:
            print('This car for family!')
        elif 0 <= self.speed < 80:
            print('This car for school!')
        elif self.speed > 150:
            print('This car is family!')
        else:
            print('Error!')
    def change_color(self):
        self.color = input('Please input new color: ')
        print(f'Brand car: {self.brand}\nName of car: {self.name}\nSpeed car: {self.speed}\nColor car: {self.color}\n')

Car1 = Vehicle('Toyota','Corolla',70,'Grey')
Car2 = Vehicle('Kia','Cerato',200,'Dark Blue')
Car3 = Vehicle('Geely','Shitness',100,'Black')
# Car1.display_info()
# Car2.display_info()
# Car3.display_info()
# Car2.change_color()

