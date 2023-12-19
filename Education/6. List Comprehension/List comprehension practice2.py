# Task 1
#Примите имя человека от пользователя, затем сгенерируйте
#имя этого человека 10 раз в новом списке.

# n = input('Enter name - ')
# list = [n for i in (range(1,11))]
# print(list, end=' ')

# Task 2 Необходимо
# все числа из этого списка, поделить на 3 и вывести новый
# список:
list2 = [18,43,9,65,12,65,24,6]
list3 = [i/3 for i in list2]
print(list3)

# Task3
# Используя этот же список сгенерируйте
# новый список из чисел, которые делимы на 3 без остатка.
list4 = [i for i in list2 if i%3==0]
print(list4)

# Task4
list5 = ['Bishkek', 'Moscow', 'Liverpool', 'Tokyo', 'Almaty']
n = 'Tokyo'
list6 = ['Совпадает' if i == n else 'Не совпадает' for i in list5]
print(list6)