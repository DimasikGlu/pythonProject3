# Task1
# 1. Запишите данный текст в файл как «lorem.txt» и прочитайте данный
# текст:
# • Строка за строкой
# • Текст целиком
# • Текст в виде списка

def write_text():
    with open("FileOperationPractice(txt)","w") as file0:
        file0.write("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
    Ipsum has been the industry's standard dummy text ever since the 1500s, when an
    unknown printer took a galley of type and scrambled it to make a type specimen
    book. It has survived not only five centuries, but also the leap into electronic
    typesetting, remaining essentially unchanged. It was popularised in the 1960s with
    the release of Letraset sheets containing Lorem Ipsum passages, and more recently
    with desktop publishing software like Aldus PageMaker including versions of Lorem
    Ipsum.""")

def readline_text():
    with open("FileOperationPractice(txt)","r") as file1:
        str1 = file1.readline()
        while str1:
            print(str1,end='')
            str1 = file1.readline()
        print(str1)

def read_text():
    with open("FileOperationPractice(txt)","r") as file2:
        content = file2.read()
        print(content)

def readinlist():
    with open("FileOperationPractice(txt)","r") as file3:
        str3 = file3.readlines()
        print(str3)

# 2. Прочтите текст из задания 1 в обратном порядке
def Task2():
    with open("FileOperationPractice(txt)","r") as file1:
        str1 = file1.readline()
        list1 = []
        list1.append(str1)
        # print(list1)
        print(str1[::-1], end='')
        while list1:
            str1 = file1.readline()
            str1 = str1.rstrip('/n')
            list1.append(str1[::-1])
            print(str1[::-1], end='')
        print(list1)

# 3. Создайте программу, в котором будет записывать введенный
# пользователем массив строк (Линию строк) и считывать его обратно
# из файла на консоль.
def Task3():
    with open("Task3.txt","a") as file3:
        print(input("Text:"),file=file3)
        text_read = open('Task3.txt','r')
        print(*text_read)
        file3.close()

if __name__=='__main__':
    # write_text()
    # readline_text()
    # read_text()
    # readinlist()
    # Task2()
    # Task3()