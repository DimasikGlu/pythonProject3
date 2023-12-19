# Task 1
# Напишите программу для построения горизонтальных столбчатых диаграмм с
# помощью символа звёздочки.
# Для этого примите определенный набор чисел от пользователя
namelist = []
for i in range(5):
    n = int(input(f'Введите число № {i+1}:'))
    namelist.append(n)
print(namelist)
for a in namelist:
    a = '*'* a
    print(a)
# Task 2 Распечатайте обратную лесенку в зависимости от числа.
n = int(input('Введите число:'))
for i in range (1,n+1):
    for j in range (1,i+1):
        j = '*'*n
    print(j, end='')
    n-=1
    print()