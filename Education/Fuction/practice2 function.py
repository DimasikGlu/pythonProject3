# 1. Давайте считать человека подростком, если его возраст находится в пределах от
# 12 до 17 лет. Напишите функцию is_person_teenager , которая помогает по
# возрасту определить является ли человек подростком или нет.
# Функция is_person_teenager принимает на вход возраст человека и
# возвращает True или False

def is_person_teenager(num):
    if 12 <= num <=  17:
        print('True')
    else:print('False')
is_person_teenager(int(input('input of age person - ')))

# 2. Напишите функцию generate_fizz_buzz_list , которая принимает одно целое
# число n - размер списка. Функция generate_fizz_buzz_list должна
# 1. обойти числа от 1 до n включительно и каждое такое число проверить
# последовательно на п2 - п5
# 2. Если число кратно и трем, и пяти, то в список заносим строку FizzBuzz
# 3. Если число кратно трем, то в список заносим строку Fizz
# 4. Если число кратно пяти, то в список заносим строку Buzz
# 5. Если число не кратно ни трем ни пяти, то в список заносим само это
# число
# В итоге функция generate_fizz_buzz_list должна вернуть сформированный
# список из n элементов. Ниже показаны примеры вызова:

list = []
def generate_fizz_buzz_list(n):
    for i in range (1,n):
        if i%3==0 and i%5 ==0:
            list.append('FizzBuzz')
        elif i%3==0:
            list.append('Fizz')
        elif i%5==0:
            list.append('Buzz')
        else: list.append(i)
    print(list)
generate_fizz_buzz_list(10)

# 3. Напишите функцию only_one_positive , которая принимает произвольное
# количество числовых аргументов и возвращает True , когда из всех переданных
# значений только одно положительное, в противном случае верните False
# Вам необходимо написать только определение функции only_one_positive

def only_one_positive(*num):
    positive_list = []
    minus_list = []
    for i in num:
        if i > 0:
            positive_list.append(i)
            if len(positive_list) == 1:
                print('True')
            else:
                print('False')
        else: minus_list.append(i)


only_one_positive(-3,-4,-5,-6,5)

# Task4 Напишите функцию, в которой принимается неопределенное кол-во чисел и
# найдите сумму этих всех чисел. Вам необходимо вернуть сумму из этой
# функции добавить к ней любое число.
def sumnum (*num1):
    for i in num1:
        sum1 = sum(num1)
    n = int(input("Введите число для добавления: "))
    print(f"Сумма всех чисел = {sum1+n}")
sumnum(5,6,7,8,9)