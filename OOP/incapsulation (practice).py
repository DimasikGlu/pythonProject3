"""
1. Переделайте данную реализацию класса под Инкапсуляцию и
для каждого аттрибута создайте Get и Set методы
class Animal:
def __init__(self, type_animal, sound):
self.type_animal = type_animal
self.sound = sound
def makeNoice(self):
print(self.sound)
dog = Animal('Dog', 'Aw-aw')
cat = Animal('Cat', 'Meow')
cow = Animal('Cow', 'Moo-moo')
duck = Animal('Duck', 'Krya-krya')
dog.makeNoice()
cow.makeNoice()
cat.makeNoice()
duck.makeNoice()"""
class Animal:
    def __init__(self, type_animal, sound):
        self.__name = type_animal
        self.__sound = sound
    def makeNoice(self):
        print(f'Result of program....\n{self.__name}\n{self.__sound}')

    def get_type_animal(self):
        print(self.__name)
    def get_sound(self):
        print(self.__sound)

    def set_type(self,newtype):
        self.__name = newtype
    def set_sound(self,new_sound):
        self.__sound = new_sound

dogs = Animal('Dog','Gav Gav!')
cats = Animal('Cat', 'Miu Miu!')
cows = Animal('Cow','Muu Muu!')
dugs = Animal('Dug','Krya Krya!')

# cats.set_type('Prince')
# cats.makeNoice()

"""2. Создайте класс Person со следующими приватными
атрибутами:
• name, age, address, can_vote (Можно будет установить
«да», «нет. По умолчанию для can_vote установлен
параметр «Да», а для возраста установлен 18)
• В конструктор нужно передавать все атрибуты, кроме
can_vote. Атрибут can_vote устанавливается в
зависимости от возраста человека.
• Создать геттер и геттер для age, name, address
• В сеттере происходит настройка возраста, затем в
зависимости от возраста can_vote становится “Да”, если
возраст человека выше либо равно 18-ти, иначе атрибут
can_vote принимает в себя «Нет».
• Создайте метод для отображение всех информаций о
человеке.
Создайте необходимые экземпляры класса и передайте в
конструктор все соответствующие параметры"""
class Person:
    def __init__(self,name,age,addres,can_vote):
        self.__name = name
        self.__age = age
        self.__addres = addres
        self.__can_vote = "Yes"
    def display_info(self):
        print(f'Name: {self.__name}\n'
              f'Age: {self.__age}\n'
              f'Addres: {self.__addres}\n'
              f'Vote: {self.__can_vote}')
    def get_name(self):
        print(self.__name)
    def get_age(self):
        print(self.__age)
    def get_addres(self):
        print(self.__addres)

    def set_vote(self):
        if self.__age >= 18:
            self.__can_vote = 'Yes'
        else: self.__can_vote = 'No'
Nikolay = Person('Nikolay', 10, 'Vatutina 17','')
Nikolay.set_vote()
Nikolay.display_info()
# Nikolay.get_age()