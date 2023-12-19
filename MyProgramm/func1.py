# Task1
# Функция, которая переворачивает в обратном направлении переданное имя:
reverseName = lambda n: print(n[::-1])


# Task2
# Функция, которая находит сумму двухзначного числа:
findsum = lambda num1: print(f'{num1//10+num1%10}')


# Task3
# Функция, которая печатает каждую вторую букву:
everySecLetter = lambda word: print(word[::-2])


# Task4 Функция, которая находит среднее значение элементов от списка:
findavg = lambda somelist: print(sum(somelist)/len(somelist))


# Task5
# # Создайте лямбду выражения, которая принимает в себя 2 числа где 2-ое
# # переданное является степенью, а 1-ое число — это то число, которую
# # необходимо возвести в степень.

Task5 = lambda num3 , num4: print(f"Число {num3} в степени {num4} - это: {num3**num4}")


# Task6
# Создайте программу, которая проверяет делятся ли два числа без остатка. Для
# того, чтобы проверить на делимость используйте лямбду выражения с
# проверкой результата с помощью if-else конструкции.

Task6 = lambda num5,num6: print(f'Делится без остатка') if num5 % num6 == 0 else print(f'Не делится без остатка')

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
def Task2_modules(num_list1):
    num_list1 = random.randint(1,16)
    name_list_random = []
    print(f'Случайная длина вашего списка людей:{num_list1}')
    print(f'Список из {num_list1} людей:')
    for i in range(1,num_list1+1):
        name_person = f'{input(str(f"Введите имя для {i} человека:"))}'
        name_list_random.append(name_person)
    print(name_list_random)

if __name__ == '__main__':
    # Task1
    reverseName('Ignat')
    # Task2
    findsum(15)
    # Task3
    everySecLetter('World')
    # Task4
    findavg([2, 5, 7, 10])
    # Task5
    Task5((int(input('Введите 1-ое число:'))), (int(input('Введите 2-ое число:'))))
    # Task6
    Task6((int(input('Введите 1-ое число:'))), (int(input('Введите 2-ое число:'))))

    # Task from modules homework
