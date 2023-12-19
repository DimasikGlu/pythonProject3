# Task1
list = ['Sergei','Putinloh','Elena','Marat','Stepan','Uson']
list_del = input('Введите слово для удаления:')
while list_del != 'Stop':
    list.remove(list_del)
    print(list)
    list_del = input('Введите слово для удаления:')
print('Удаление завершено')

# Task2
listNum = [23, 45, 4, 5, 12, 4, 5, 7, 15, 21, 78, 41]
num1 = listNum[0]%3
num = len(listNum)
listNum2 = listNum[0]
while num != 0:
     num = len(listNum)
     if num == 0:
         break
     num3 =  listNum[0]%3
     if num3 <=0:
         print(f'Число делится на три: {listNum[0]}')
     listNum.remove(listNum[0])

# task 3
namelist = ['Hello', 'There', 'World', 'Bishkek', 'Tokyo', 'Almaty']
i = 'o'
numbers = 0
while numbers <= len(namelist):
    if numbers == len(namelist):
        break
    word1 = namelist[numbers]
    if i in word1:
        namelist.remove(word1)
    numbers +=1
print(namelist)

