# Task 1
# num1 = int(input('Число № 1:'))
# num2 = int(input('Число № 2:'))
# num3 = int(input('Число № 3:'))
# if num1 == num3 < num2:
#     print(f"Наибольшое число № 2 со значением = {num2}")
# elif num1 == num3 > num2:
#     print(f"Наибольшое число № 1,3 со значением = {num1}")
# elif num1 == num2 > num3:
#         print(f"Наибольшое число № 1,2 со значением = {num2}")
# elif num1 == num2 < num3:
#         print(f"Наибольшое число № 3 со значением = {num3}")
# elif num1 < num2 == num3:
#         print(f"Наибольшое число № 2,3 со значением = {num2}")
# elif num1 > num2 == num3:
#         print(f"Наибольшое число № 1 со значением = {num1}")
# elif num1 > num2 > num3:
#     print(f"Наибольшое число № 1 со значением = {num1}")
# elif num1 < num2 < num3:
#     print(f"Наибольшое число № 3 - {num3}")
# elif num1 > num2 < num3:
#     print(f"Наибольшое число № 3 со значением = {num3}")
# elif num1 < num2 > num3:
#     print(f"Наибольшое число № 2 со значением = {num2}")
# elif num1 < num2 < num3:
#     print(f"Наибольшое число № 2 со значением = {num2}")
# else: print(f"Введенные числа c одиннаковыми значениями = {num1}")

# Task 2
# city1 = str(input('Введите город № 1:'))
# city2 = str(input('Введите город № 2:'))
# if city1[len(city1)-1] == city2[0].lower():
#     print('Good')
# else: print('Bad')
# Task 3
month = int(input("Введите номер месяца:"))
# if 1 <= month <= 12:
#     month = month
# else: print('Номер месяца указан неверно')
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print('В месяце 31 день')
    case 4 | 6 | 9 | 11:
        print('В месяце 30 дней')
    case 2:
        print('В месяце 28 дней')
    case _:
        print('Номер месяца указан неверно')
