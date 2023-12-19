"""1. Создайте класс, который называется Dog, принимающий в качестве атрибута
через конструктор - имя, породу, возраст и вес.
• Создайте метод для отображения всех информаций о собаке
• Создайте метод, который бы позволил по весу определить подходит ли
определенная собака для перевозки в самолете, если вес собаки меньше 3
кг, то ваш метод должен возвращать True, иначе False
После создания класса, вам необходимо создать 3 экземпляра на основе этого
класса и вызвать эти два метода."""

class Dog:
    def __init__(self, name, breed, weight):
        self.name_dog = name
        self.breed_dog = breed
        self.weight_dog = weight
    def display_info(self):
        print(f'Имя собаки - {self.name_dog}\n'
              f'Порода собаки {self.name_dog} - {self.breed_dog} \n'
              f'Вес собаки {self.name_dog} - {self.weight_dog} kg')
    def check_weight(self):
        self.weight_dog = int(self.weight_dog)
        if self.weight_dog < 3:
            print(f'True - {self.name_dog}')
        else:
            print(f'False - {self.name_dog}')


Sachi = Dog('Sachiko', 'Shiba inu', 11)
Tishka = Dog('Tishka', 'Bigle', 15)
Kefir = Dog('Kefir', 'JackRassel', 2)

# Sachi.display_info()
# Tishka.display_info()
# Kefir.display_info()
#
# Sachi.check_weight()
# Tishka.check_weight()
# Kefir.check_weight()

"""2. Создайте класс Alphabet, где в качестве аргумента через конструктор
принимаются следующие аргументы – Язык и список букв.
Вам необходимо в этом классе создать два метода:
• Метод, который бы напечатал все буквы из данного алфавита
• Метод, который бы посчитал количество букв из алфавита"""

class Alphabet:
    def __init__(self, language, alphabet_list):
        self.lang = language
        self.alpha_list = alphabet_list
    def print_alpha(self):
        print(f'Language is {self.lang}')
        for i in self.alpha_list:
            print(i.lower(), end=" ")
        print()
    def len(self):
        print(len(self.alpha_list))

lang = Alphabet('Russian',['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
                           'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ',
                           'Ы', 'Ь', 'Э', 'Ю', 'Я'])
lang.print_alpha()
lang.len()