# Task1
# def name(name):
#     try:
#         name = input('input name:')
#         print ('Sucsefull!.....')
#         print(f'Привет {name}, добро пожаловать в нашу программу!')
#     except:
#         print('Uncorrect name, try again please')
#         name = input('input name again:')
# name(name)

# Task2
# def exponentiation(num):
#     try:
#         num = int(input('input number:'))
#         print ('Sucsefull!.....')
#         print(f'{num**2} {num**3}')
#     except:
#         print('Uncorrect num, try again please')
#         num = int(input('input number:'))
#         print(f'{num ** 2} {num ** 3}')
#
# exponentiation()

# Task3
def calcAvg():
    try:
        num1 = int(input('input number1:'))
        num2 = int(input('input number2:'))
        num3 = int(input('input number3:'))
        print('Sucsefull!.....')
        print(f'{(num1+num2+num3)/3}')
    except:
        print('Uncorrect num, try again please')
        num1 = int(input('input number1:'))
        num2 = int(input('input number2:'))
        num3 = int(input('input number3:'))
        print('Sucsefull!.....')
        print(f'{(num1+num2+num3)/3}')

calcAvg()


# # Task4
# def division(num1,num2,num3=1):
#     print(f'Деление числа № 1 на 2: {num1/2}\n '
#           f'Деление числа № 2 на 3: {num2/3}\n'
#           f'деление числа № 3 на : {num3/1}')
# division(4,6,7)
#
# # Task5
# def range_values (num1,num2,num3):
#     for i in range(num1,num2,num3):
#         print(i,end=' ')
#
# range_values(int(input('Введите начало отсчета: ')),int(input('Введите конец отсчета: ')),int(input('Введите шаг отсчета: ')))
#
# # Task6
# list = []
# list1 = []
# list2 = []
# def list_sorted(*list):
#     for i in list:
#         if i%2 == 0:
#             list1.append(i)
#         else:
#             list2.append(i)
#     print(f'Список № 1 (chet) - {list1}\n'
#           f'Список № 2 (nechet) - {list2}')
#
# list_sorted(1,2,3,4,5,6,7,8,9,10)