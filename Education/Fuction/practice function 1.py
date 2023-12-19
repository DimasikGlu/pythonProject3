# Task1
def name(name):
    print(f'Привет {name}, добро пожаловать в нашу программу!')
name("Петя")

# Task2
def exponentiation(num):
    print(f'{num**2} {num**3}')
exponentiation(int(input('Введите число:')))
# Task3
def calcAvg(num1,num2,num3):
    print(f'{(num1+num2+num3)/3}')
calcAvg(2,4,6)
# Task4
def division(num1,num2,num3=1):
    print(f'Деление числа № 1 на 2: {num1/2}\n '
          f'Деление числа № 2 на 3: {num2/3}\n'
          f'деление числа № 3 на : {num3/1}')
division(4,6,7)

# Task5
def range_values (num1,num2,num3):
    for i in range(num1,num2,num3):
        print(i,end=' ')

range_values(int(input('Введите начало отсчета: ')),int(input('Введите конец отсчета: ')),int(input('Введите шаг отсчета: ')))

# Task6
list = []
list1 = []
list2 = []
def list_sorted(*list):
    for i in list:
        if i%2 == 0:
            list1.append(i)
        else:
            list2.append(i)
    print(f'Список № 1 (chet) - {list1}\n'
          f'Список № 2 (nechet) - {list2}')

list_sorted(1,2,3,4,5,6,7,8,9,10)