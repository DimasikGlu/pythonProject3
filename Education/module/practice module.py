# Task1
"""Импортируйте модуль math и выполните следующие действия:
• выведите в консоль число π;
• используйте псевдоним для модуля math - m;
• получите число по модулю;
• выведите число e."""
import math as m
import random

print(m.pi)
print(abs(-50))
print(m.fmod(15,2))
print(m.e)

# Task2
# Из модуля math импортируйте в проект следующее:
# • значение числа π
# • функцию ceil
# • Для функции сделайте псевдоним «c».

from math import pi
from math import ceil as c
print(c(13.3))

# Task3
# 3. Выберите случайное число из данного списка
# [12,43,4,3,23]
list1 = [12,43,4,3,23]
print(random.choice(list1))

# Task4
# Сгенерируйте случайное число в промежутке от 1 до 100
print(random.randint(0,101))

# Task5
# Сгенерируйте список из 10 чисел в промежутке от 1-го 50
list2 = []
for i in range(10):
    list2.append(random.randrange(0,51))
print(list2)


# создание библиотеки и вызов функция
# from MyProgramm.func1 import findavg
# findavg([50,25,75,100])


