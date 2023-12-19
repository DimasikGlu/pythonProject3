# Task1
# Добавьте в заданное множество, заданный список:
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(sampleSet)

# Task2
# Необходимо вернуть схожий результат взятый из двух разных множеств:
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# # result = {40, 50, 30} - this is answer
# result = set1.intersection(set2)
# print(result)

# Task3 Даны два множества, необходимо обновить первое множество с элементами,
# которые есть только в первом элементе, но нету во втором элементе.
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# # set1 = {10, 30} - answer
# set1.difference_update(set2)
# print(set1)

# Task4
# Создайте множество из двух элементов: 1 и 3.
# Выполните действия:
# • добавьте один новый элемент;
# • добавьте сразу несколько элементов в множество;
# • добавьте список и еще одно множество в ваше изначально созданное
# множество.
# set_task4 = {1,3}
# set_task4.add(2)
# print(set_task4)
# set_task4.update({4,5,6})
# print(set_task4)
# set_task4.update([7,8,9],{100,200,300})
# print(set_task4)

# # Task5
# Создайте set и frozenset.
# Объедините оба множество в одно целое.
# Выполните операции:
# к объединенному множеству добавьте элемент 2 и 5;
# удалите число 2, а также первый элемент в множестве.
set_task5 = {1,3}
set_task5_1 = frozenset({4,6})
set_task5_res = set_task5.union(set_task5_1)
print(set_task5_res)
set_task5_res.update({2,5})
print(set_task5_res)
set_task5_res.remove(2)
print(set_task5_res)
set_task5_res.pop()
print(set_task5_res)

