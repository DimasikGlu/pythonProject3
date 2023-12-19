"""1. Передайте в функцию возраст 3-х людей в качестве аргумента для *args, имена
этих людей в качестве **kwargs.
• Вычислите суммарный возраст этих людей
• Отобразите их имена"""


def people_age(*args, **kwargs):
    list1 = []
    for i in args:
        list1.append(i)
    sum_age = sum(list1)
    print(f"Суммарный возраст всех людей:{sum_age}")
    for n in kwargs.values():
        print(f"{n}",end=" ")

args = (30, 15, 40)
kwargs = {"name1": "Alena", "name2": "Ignat", "name3": "James"}
people_age(*args,**kwargs)

# 2. Создать лямбда выражение, которая возводит в квадрат переданное ей число
square = lambda num: print(num**2)
square(2)

# 3. Создать лямбду выражения, которая возвращает среднее значение среди 4
# переданных чисел
def sred(*num1): print(sum(num1)/4)

sred(3,4,5,2)

def sum_pay(num2):
    num2 =int(input('Введите сумму для оплаты:'))
    if 1999 >= num2 >= 1000:
        print(f"Сумма скидки составляет 2% от {num2} сом:{num2*98/100} сом")
    elif 4999 >= num2 >= 2000:
        print(f"Сумма скидки составляет 5% от {num2} сом:{num2*95/100}")
    elif 9999 >= num2 >= 5000:
        print(f"Сумма скидки составляет 10% от {num2} сом:{num2*90/100}")
    elif num2 >= 10000:
        print(f"Сумма скидки составляет 20% от {num2} сом:{num2 * 80/100}")
    else:print(f"Извините для суммы {num2} сом скидки нет.")

sum_pay(1)
