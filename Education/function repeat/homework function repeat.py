# Task1
"""Создайте функцию, которая принимает в качестве параметра список или кортеж
и затем возвращает словарь в, которой есть информация о том, какое
количество раз каждый элемент в списке/кортеже дублируется."""
# def list_create(list1):
#     for i in list1:
# list2 = []
# list1 = ['Aglaya','Francisc','Safron','Francisc','Petya','Nargis','Petya']
# for i in list1:
#     num = list1.count(i)
#     list2.append(num)
# dict1 = dict(zip(list1,list2))
# print(dict1)

# Task2
"""Создайте функцию, которая принимает в качестве аргумента строку, эта
функция должна записать все гласные буквы в отдельный один список, а
согласные в другой. После чего вам необходимо скомбинировать эти два
списка."""
# def str(string):
#     list3 = []
#     list4 = []
#     gl = ['a','e','i','o','y','u']
#     for i in string:
#         if i in gl:
#             list3.append(i)
#         else:list4.append(i)
#     list5 = [list3,list4]
#     print(list5)
# str('Hello world')

# Task3
"""Создайте функцию, которая принимает в качестве аргумента список из списков
и возвращает индекс внутреннего списка у, которой самое большое среднее
значение"""
myList = [
[3,4,5,12],
[7,4,6,2],
[3,2],
[5,6,7,10,3]
]
def findMaxMean(myList):
    list_num = []
    for i in myList:
        avg = (sum(i)/len(i))
        list_num.append(avg)
    Maxnum = max(list_num)
    print(f'Index max avg number - {list_num.index(Maxnum)}')
    # print(f'Индекс - {list_num.index(Maxnum)}')

findMaxMean(myList)

