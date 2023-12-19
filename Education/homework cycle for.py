# Task 1
num = int(input('Сколько кол-во записей создать:'))
namelist = list()
for i in range(num):
    i = input('Введите имя:')
    namelist.append(i)
print(namelist)
# Task 2
a = int(input('Введите число № 1:'))
b = int(input('Введите число № 2:'))
for i in range(a, b + 1):
    if a > b:
        print('Ошибка ввода второе число, д.б. больше')
    print(f'Число- {i}; его квадрат = {i**2}; его куб = {i**3}')
# Task 3
a1 = int(input('Введите число № 1:'))
b1 = int(input('Введите число № 2:'))
for i in range(a1,b1+1):
    if i%5==0 and i%3==0 :
        print(f'FizzBuzz, число - {i}')
    elif i%3==0:
        print(f'Fizz, число - {i}')
    elif i%5 == 0:
        print(f'Buzz, число - {i}')
    else: print(f'число в ост. случаях - {i}')
