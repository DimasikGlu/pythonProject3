#1. Напишите программу на Python для чтения последних n строк"
#файла. Количество последних строк принять от пользователя."
def Task1():
    num1 = 0
    with open("By HW.txt","r") as file1:
        str1 = file1.readline()
        while str1:
            str1 = file1.readline()
            num1 = num1+1
        print(f"Кол-во строк:{num1}")
        num_user = int(input("Please input num for read: "))
        num_user = num_user-1
        file1.seek(0)
        str_user = file1.readlines()
        if 0 <= num_user <= 9:
            print("".join(str_user[num_user:]))
        else: print('Range this num is 9, please try again')

# 2. Напишите программу на Python для подсчета количества строк в
# текстовом файле.
def Task2():
    num2 = 0
    with open("By HW.txt","r") as file2:
        str1 = file2.readline()
        while str1:
            str1 = file2.readline()
            num2 = num2+1
        print(f"Кол-во строк:{num2}")

# 3. Напишите программу на Python для чтения случайной строки из
# файла.
import random
def Task3():
    with open("By HW.txt", "r") as file3:
        num3 = random.randint(1,9)
        str_user = file3.readlines()
        print("".join(str_user[num3:]))

# 4. Примите от пользователя список из 10 работников. Запишите
# данный список в отдельный файл как workers.txt. Имена каждого из
# сотрудников должно быть в отдельной строке.
def Task4():
    list_names = []
    num4 = 0
    for i in range(10):
        num4 = num4 + 1
        i = f'{input(str(f"Input name №{num4}: "))}'
        list_names.append(i)
    print(f"Your names list:{list_names}")
    with open("workers.txt","a") as file4:
        for i in list_names:
            file4.write(f"{i}\n")

# 5. Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file), которая
# выводит слово, имеющее максимальную длину (или список слов,
# если таковых несколько)."""
def longest_words():
    list5 = []
    longest_size = 0
    longest_word = ""
    with open("article.txt","r",encoding="utf-8") as file5:
        str5 = file5.readline()
        list5.append(str5)
        for i in str5:
            str5 = file5.readline()
            list5.append(str5)
        for word in list5:
            if len(word) > longest_size:
                longest_word = word
                longest_size = len(word)
        print(longest_word)


if __name__=='__main__':
    # Task1()
    # Task2()
    # Task3()
    # Task4()
    # longest_words()
