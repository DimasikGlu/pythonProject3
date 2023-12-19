# def my_simple_decor(function_to_decorate):
#     def func_wrap():
#         print('первая функция')
#         function_to_decorate()
#         print("Последняя функция")
#
#     return func_wrap
#
# @my_simple_decor
# def my_simple_decor2():
#     print('Функция в гуще событий')

""" Задание № 1:
Создайте простую функцию, которая принимает в качестве аргумента список и
возвращает ее
Создайте декоратор, который принимает на вход функцию с задания No1 и
записывает в отдельный файл, который называется ‘resultList.txt’"""
import pandas as pd

list1 = [5,4,6,7,8,3,2,1,5,7]

def Task1(fuction):
    def wrapper1():
        print(f'Show your list: {list1}')
        fuction()
        print('---------The list is over----------')
    return wrapper1

# @Task1
# def function():
#     with open("resultList(txt)", "w") as file1:
#             for i in list1:
#                 file1.write(f'{i} ')

"""Используя созданную простую функцию в первом задании примените к ней уже
другой декоратор, который записывает в отдельный Экзель файл следующие
результаты:
• Количество элементов внутри списка
• Среднее значение
• Сумма
Пример реализации простой функции и результат Экзель файла:"""
import pandas as pd
@Task1
def function():
    Df1 = pd.DataFrame({'Number of values': [len(list1)],
                        'Average of values': [sum(list1)/len(list1)],
                        'Sum of values': [sum(list1)]})
    Df1.to_excel('./resultList.xlsx',sheet_name='List1', index=False)
    # def Task1():
    #     df1 = pd.DataFrame({'Name': ['Dima', 'Gena', 'Petya', 'Zina', 'Nina', 'Sasha'],
    #                         'Age': [27, 33, 50, 20, 25, 35],
    #                         'Salary': [10000000, 15000, 10000, 2000, 30000, 10030],
    #                         'Position': ['freedom', 'ingener', 'Slesar', 'kasir', 'blogger', 'blogger', ]})
    #     df1.to_excel('./workers1.xlsx', sheet_name='Workers_sheet1', index=False)

if __name__=='__main__':
    function()
    # Task2()
    # Task3()
    # Task4()