# Task 1
list_num = list()
i = int()
while i != 'stop':
    i = input('Элемент для списка (stop для остановки):')
    list_num.append(i)
list_num.remove(list_num[-1])
print(list_num)
search_str = input('Элемент для поиска:')
for i in range(len(list_num)):
    i = list_num.index(search_str)
print(f'Номер индекса, в котором находится 32:{i}')

# Task 2
str1 = str(input('Буква:')).lower()
text = str(input('Введите предложение:')).lower().split()
for i in text:
    if str1 in i:
        print(i)
