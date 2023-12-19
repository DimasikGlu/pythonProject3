"""1. Дано натуральное число N и последовательность из N элементов. Требуется
вывести эту последовательность в обратном порядке.
Входные данные
Программа принимает на вход натуральное число N (N ≤ 103). Во второй строке
через пробел идут N целых чисел, по модулю не превосходящих 103 - элементы
последовательности.
Выходные данные
Ваша задача вывести заданную последовательность в обратном порядке."""
list2 = [10, 20, 30, -150]
def Recursive1(n):
    for n in list2:
        if abs(n) <= 103:
            continue
        else:
            list2.remove(n)
            return Recursive1(n)
    for j in list(reversed(list2)):
        print(j,end=' ')

"""2. Напишите функцию list_sum_recursive, которая принимает на вход список из
целых чисел и возвращает сумму элементов переданного списка. Не забывайте,
что реализовать это нужно при помощи рекурсии.
Ваша задача только написать определение функции list_sum_recursive
Пример ввода:
1 2 3
Пример вывода:"""
def list_sum_recursive(*list):
    list_sum = [int(a) for a in input().split()]
    return print(sum(list_sum))

"""3. Представьте, что у нас есть список целых чисел неограниченной вложенности.
То есть наш список может состоять из списков, внутри которых также могут
быть списки. Ваша задача превратить все это в линейный список при помощи
функции flatten. К примеру:
flatten([1, [2, 3, [4]], 5]) # вернет [1,2,3,4,5]
flatten([1, [2,3], [[2], 5], 6]) # вернет [1,2,3,2,5,6]"""
def flatten(lst):
    if len(lst) == 0:
        return lst
    if isinstance(lst[0], list):
        return (flatten(lst[0])) + flatten(lst[1:])

    return lst[:1] + flatten(lst[1:])

    # i = 0
    # list3 = []
    # if range(len(list)) != 0:
    #     list3.append(list[i])
    #     i+=1
    #     return flatten(list[len(list)][i][i])
    # else: return print('complete!')
    # print(list3)

if __name__=='__main__':
    # Recursive1([10, 20, 30, -150])
    # list_sum_recursive()
    print(flatten([[1],[2]]))
