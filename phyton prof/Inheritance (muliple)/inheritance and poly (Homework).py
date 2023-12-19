"""1"""
class Teacher():
    def __init__(self,FIO,experience,theme,quantity):
        self.FIO = FIO
        self.experience = experience
        self.theme = theme
        self.quantity = quantity
    def displayInfo(self):
        print(f"FIO: {self.FIO}\n"
              f"Experience: {self.experience}\n"
              f"Lesson theme: {self.theme}\n"
              f"Quantity: {self.quantity}")
teacher1 = Teacher('Zina Valerievna Shtoporova', '12 years', 'Verbs', 20)
# teacher1.displayInfo()
class DrawingTeacher(Teacher):
    def __init__(self,FIO,experience,theme,quantity,figure):
        super().__init__(FIO,experience,theme,quantity)
        self.figure = figure
    def findSimiliarObject(self):
        if self.figure == 'triangle':
            print('This figure like egyptian pyramid')
        elif self.figure == 'square':
            print('This figure like Sponge Bob')
        else: print('Good figure!')
    def displayInfo(self):
        print(f"Information about Drawing teacher...\nFIO: {self.FIO}\n"
              f"Experience: {self.experience}\n"
              f"Lesson theme: {self.theme}\n"
              f"Quantity: {self.quantity}\n"
              f"Figure: {self.figure}")
# test1 = DrawingTeacher('Zina Valerievna Shtoporova', '12 years', 'Verbs', 20,'triangle')
# test1.displayInfo()
class GeographyTeacher(Teacher):
    def __init__(self,FIO,experience,theme,quantity,country):
        super().__init__(FIO,experience,theme,quantity)
        self.country = country
    def displayInfo(self):
        print(f"Information about Geography teacher...\nFIO: {self.FIO}\n"
              f"Experience: {self.experience}\n"
              f"Lesson theme: {self.theme}\n"
              f"Quantity: {self.quantity}\n"
              f"Country: {self.country}")
    def findCapitalcity(self):
        if self.country == 'USA':
            print('Capital of USA - Washington')
        elif self.country == 'Italy':
            print('Milan')
        else: print('None information')
class MathTeacher(Teacher):
    def __init__(self,FIO,experience,theme,quantity,*num):
        super().__init__(FIO,experience,theme,quantity)
        self.num = num
    def displayInfo(self):
        print(f"Information about Math teacher...\nFIO: {self.FIO}\n"
              f"Experience: {self.experience}\n"
              f"Lesson theme: {self.theme}\n"
              f"Quantity: {self.quantity}\n"
              f"Sum of num: {self.num}")
    def findAvarage(self):
        print(f"Average: {sum(self.num)}")

# math1 = MathTeacher('Zina Valerievna Shtoporova','12 years','Verbs',20,15,20,20)
# math1.findAvarage()
"""2. Создайте класс MathGeographyTeacher для человека, который является
одновременно и учителем математики, и учителем географии. Данный класс
должен наследоваться от двух классов: от MathTeacher и от GeographyTeacher.
Создайте конструктор для этого класса.
Дополнительно в этом классе создайте метод introducing(), где данный
учитель говорит: «Меня зовут {self.name} и я веду Математику и Географию»"""
class MathGeographyTeacher(GeographyTeacher,MathTeacher):
    def __init__(self,FIO,experience,theme,quantity,country,*num):
        GeographyTeacher.__init__(self,FIO,experience,theme,quantity,country)
        MathTeacher.__init__(self,FIO,experience,theme,quantity,*num)
    def introducing(self):
        print(f"Hi, my name is {self.FIO}. Im your teacher Math and Geography")
mathgeo = MathGeographyTeacher('Zina Valerievna Shtoporova','12 years','Verbs',20,'USA',15,20)
mathgeo.introducing()