num = int (input('Введите число № 1:'))
num10 = int (input('Введите число № 2:'))
if num > num10:
    print ('Первое число больше второго')
elif num < num10:
    print('Второе число больше первого')
else:
    print('Числа равны')
# 2 task
operation = int(input('Введите номер операции:'))
if operation == 1:
    print('Выбранная операция - сложение')
elif operation == 2:
    print('Выбранная операция - вычитание')
elif operation == 3:
    print('Выбранная операция - умножение')
else:
    print('Операция не определена')
# 3 task
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
# if num1 > num2: # в случае если пользователь указывает первое число меньше второго, числа меняются местами
# во избежание отрицаительных значения
#     num1 = num1
# elif num2 < num1:
#     num1,num2 = num2,num1
# else: num1 = num1
operation = int(input('Введите номер операции, где: \n1.Сложение\n2.Вычитание\n3.Умножение\nВведите:'))
if operation == 1:
    print(f'Результат операции сложения:{num1+num2}')
elif operation == 2:
    print(f'Результат операции вычитания:{num1-num2}')
elif operation == 3:
    print(f'Результат операции умножения:{num1*num2}')
else:
    print('Результат: Неверно определена операция')
# 3 Task
num3 = int(input('Введите число для определения четности:'))
if num3%2 == 0:
    print("Число № 3 является четным")
else: print("Число № 3 является нечетным")







