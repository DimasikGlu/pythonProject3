"""1. Создайте класс Student, которая принимает через конструктор следующие аргументы:
• name - имя студента
• payment - сумма контракта
• marks - словарь с оценками по разным предметам, где ключами выступают название предметов
• список задолженностей по различным предметам
Внутри данного класса создайте следующие магические методы:
__str__ - для вызова имени студента
__add__ - для добавления к payment другую сумму контракта, либо
для суммирования контрактов двух студентов
__sub__ - для вычитания контракта одного студента от контракта другого студента
__mul__ - для умножение контракта студента на определенное значение
__lt__/__gt__/__le__/__ge__ /__eq__ - для сравнения средних оценок двух студентов или
сравнение средней оценки с другой любой цифрой"""
class Student():
    def __init__(self,name,payment,marks,dolgi):
        self.name = name
        self.payment = payment
        self.marks = marks
        self.dolgi = dolgi
    def display(self):
        print(f"{self.name},{self.payment},{self.marks},{self.dolgi}")
    def __str__(self):
        return f"Name student: {self.name}"
    def __add__(self,other):
        # self.add_payment = int(input("Please input num: "))
        # if self.add_payment > 0:
        #     return self.payment + self.add_payment
        if isinstance(other, int):
            return self.payment + other

    def __sub__(self, other):
        if self.payment >= other.payment:
            return self.payment - other.payment
        return other.payment - self.payment
    def __mul__(self,num_multiply):
        return self.payment * num_multiply
    def __lt__(self, other):
        return sum(self.marks.values())/len(self.marks.values()) < sum(other.marks.values())/len(other.marks.values())
    def __gt__(self, other):
        return sum(self.marks.values())/len(self.marks.values()) > sum(other.marks.values())/len(other.marks.values())
    def __le__(self,other):
        return sum(self.marks.values())/len(self.marks.values()) <= sum(other.marks.values())/len(other.marks.values())
    def __ge__(self, other):
        return sum(self.marks.values())/len(self.marks.values()) >= sum(other.marks.values())/len(other.marks.values())
    def __eq__(self, other):
        return sum(self.marks.values())/len(self.marks.values()) == sum(other.marks.values())/len(other.marks.values())

student1 = Student('Nikolay Shishkin',10000,{'Physics':5, 'Math':4,'Geography':3},['Chemistery','Biology'])
student2 = Student('Igor Kozhemyakin',20000,{'Literature':5, 'Math':5,'Geography':5},['Graphycs',''])
# print(student1 + student2)
print(student1 - student2)
