# Task1 Необходимо сгенерировать список, возведенных вквадрат в
# промежутке между 1 и 10
list1 = [i**2 for i in range(1,11)]
print(list1)
# Task2 Есть текст со словом “I love programming so much and I would like to
# improve my skills”, вам необходимо из части этого текста
# сгенерировать список с буквами следующего вида:
text = 'I love programming so much and I would like to improve my skills'
list2 = [i for i in text]
print(list2)

# task3 Примите от пользователя любое слово и сгенерируйте новый
# список, состоящий только из согласных букв принятого от
# пользователя слова.
i = input('Введите слово: ')
k = ['a','e','y','u','i','o']
list3 = [n  for n in i if n not in k ]
print(list3)

# task4
listnum1 = [2,3,4,5]
listnum2 = [20,41,28,56]
listres = ['true' if listnum2[i]%listnum1[i] == 0 else 'false' for i in range(4)]
print(listres)
