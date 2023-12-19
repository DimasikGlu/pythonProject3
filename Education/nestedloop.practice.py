# task 1
for i in range(1,10):
    for j in range (1,10):
        sum = i*j
        print(f'{i}*{j} = {sum}')
# task 2
n = int(input('Введите кол-во уровней: '))
for i in range(1,n+1):
    for j in range(1,i):
        print(j, end=' ')
    print(i)
# Task 3
a = int(input('Введите кол-во строк: '))
b = int(input('Введите кол-во столбцов: '))
namelist = []
for i in range(a):
    templist = []
    for j in range(b):
        num = int(input(f'Enter number {j+1} for {i+1}:'))
        templist.append(num)
    namelist.append(templist)
print('-'*30)
print(namelist)
for a in namelist:
    for num in a:
        print(num, end=" ")
    print()
