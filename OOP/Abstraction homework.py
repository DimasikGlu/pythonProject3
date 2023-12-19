"""1. Есть некий Абстрактный класс Car у которого есть абстрактный
метод brake(), gas() и приватные поля:
• model;
• color;
• maxSpeed;
Реализуйте и переопределите вышеописанные методы в классах
наследниках Sedan, SportCar, FamilyCar"""
from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self,model,color,maxSpeed):
        self._model = model
        self._color = color
        self._maxSpeed = maxSpeed
    @abstractmethod
    def brake(self):
        return self._model
    @abstractmethod
    def gas(self):
        pass

class Sedan(Car):
    def __init__(self,model,color,maxSpeed):
        super().__init__(model,color,maxSpeed)
    def brake(self):
        super().brake()
        print('Sedan is braking')
    def gas(self):
        super().gas()
        print('Include gas on sedan ')
class Sportcar(Car):
    def __init__(self,model,color,maxSpeed):
        super().__init__(model,color,maxSpeed)
    def brake(self):
        super().brake()
        print('Sportcar is braking')
    def gas(self):
        super().gas()
        print('Include turbogas on Sportcar')
class FamillyCar(Car):
    def __init__(self,model,color,maxSpeed):
        super().__init__(model,color,maxSpeed)
    def brake(self):
        super().brake()
        print('Sportcar is slow-slow braking')
    def gas(self):
        super().gas()
        print('Include of minigas on Sportcar')
sedan1 = Sedan('1','black',100)
# print(sedan1.brake())
# sedan1.gas()
# sportcar = Sportcar('Turbo','Red',1000)
# sportcar.gas()

"""2. Есть абстрактный класс Person, в нем содержится абстрактный
метод calculateMyExpenses(), whereToEat(), earnMoney()
В классах наследниках Student, BankWorker, Doctor необходимо
переопределить вышеописанные методы для каждого класса по
своему."""
from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def calculateMyExpenses(self):
        pass
    @abstractmethod
    def whereToEat(self):
        pass
    @abstractmethod
    def earnMoney(self):
        pass

class Student(Person):
    def __init__(self,position,bank):
        self.position = position
        self.bank = bank
    def info(self):
        print(f"Position: {self.position}\nBank: {self.bank}$")
    def calculateMyExpenses(self,expenses):
        self.expens = expenses
        return self.bank == self.bank-self.expens-self.pricetofood
    def whereToEat(self, priceFood):
        self.pricetofood = priceFood
        print(f"{self.position} eats in cafe for price is {self.pricetofood}$")
    def earnMoney(self):
        pass

student = Student('student',1000)
student.info()