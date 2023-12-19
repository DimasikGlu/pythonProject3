# Task1
# Попробуйте сделать следующих заданий заданий модуль и вызвать из другого
# файла.
# 1. У вас есть список из 8 людей:
# listNames = ['Esen', 'Timur', 'Burul', 'Adik', 'Bermet', 'Asan', 'Elena', 'Murat' ]
# Они все желают поехать в горы.
# Вам необходимо создать программу, которая случайным образом удалит 4-х людей
# со списка, так как в легковую машину поместятся только 4 человека (не включая
# водителя).
import random
def Task1_modules(listNames):
    listNames = ['Esen', 'Timur', 'Burul', 'Adik', 'Bermet', 'Asan', 'Elena', 'Murat' ]
    for i in range(0,4):
        name_delete = (random.choices(listNames))
        name_delete1 = name_delete[0]
    # print(name_delete1)
        (listNames.remove(name_delete1))
    print(listNames)


# # Task2
# # Создайте программу, которая составляет список людей со случайной длиной в
# # промежутке от 1-го до 15-ти
def Task2_modules (num_list1):
    num_list1 = random.randint(1,16)
    name_list_random = []
    print(f'Случайная длина вашего списка людей:{num_list1}')
    print(f'Список из {num_list1} людей:')
    for i in range(1,num_list1+1):
        name_person = f'{input(str(f"Введите имя для {i} человека:"))}'
        name_list_random.append(name_person)
    print(name_list_random)

"Вызов функций из модуля"
from MyProgramm.func1 import Task1_modules
Task1_modules(['Esen', 'Timur', 'Burul', 'Adik', 'Bermet', 'Asan', 'Elena', 'Murat'])

from MyProgramm.func1 import Task2_modules
Task2_modules(random.randint(1,16))


# if __name__ == '__main__':
#     Task1_modules(['Esen', 'Timur', 'Burul', 'Adik', 'Bermet', 'Asan', 'Elena', 'Murat'])
#     Task2_modules(random.randint(1,16))
