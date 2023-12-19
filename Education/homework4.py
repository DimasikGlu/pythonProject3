# Task 1
# a
num = int(input('Введите число:'))
if num > 2 and num < 9:
    print('Число больше 2 и меньше 9')
else:
    print('Неизвестное число')
# b
num2 = int(input('Введите число:'))
res = print('Число больше 2 и меньше 9') if num2> 2 and num2 < 9 else print('Неизвестное число')

# Task 2
weight = int(input('Введите вес посылки для расчета стоимости доставки - '))
if weight > 0 and weight <= 2:
    print(f"Cтоимость доставки груза составляет - {weight*3.5} $")
elif weight >= 3 and weight <= 5:
    print(f"Cтоимость доставки груза составляет - {weight*5.5}$")
elif weight >= 6 and weight <= 10:
    print(f"Cтоимость доставки груза составляет - {weight*7}$")
elif weight > 10 and weight < 50:
    print(f"Cтоимость доставки груза составляет - {weight *10}$")
else: print("Посылка не может быть отправлена, вес превышает допустимые значения")

# Task 3
number = int(input('Введите число для проверки:'))
if number%2 ==0:
    print('Перезапустите программу.')
else: print('Число является нечетным.')