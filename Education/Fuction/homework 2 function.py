# 1. Напишите функцию info_kwargs, которая принимает произвольное количество
# именованных аргументов.
# Функция info_kwargs должна распечатать именованные аргументы в каждой
# новой строке в виде пары <Ключ> = <Значения>, причем ключи должны
# следовать в алфавитном порядке. Пример работы смотрите ниже

def info_kwargs(**kwargs):
        for i in sorted(kwargs):
                print(i,'=',kwargs[i])

info_kwargs(first_name="John", last_name="Doe", age=33)

def format_name_list(*args):
        list1=[]
        list2 = []
        for i in args:
                for n in i.values():
                        list1.append(n)
        if len(list1) == 1:
                print("".join(list1))
        elif len(list1)== 2:
                print(" и ".join(list1))
        elif len(list1)> 2:
                for a in range(len(list1)-1):
                        list2.append(list1[a])
                list2 = " , ".join(list2)
                print(f"{list2} и {list1[-1]}")

format_name_list({'name': "Bart" },{'name': "Ignat"},{'name': "Garik"},{'name': "Petya"})
