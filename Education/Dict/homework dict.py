# Task1 Необходимо объединить заданные словари в один-единый словарь:
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = dict1 | dict2
print(dict3)

# Task2 Выведите на экран значения ключа history:
sampleDict = {
    "class": {"student": {"name": "Mike", "marks": {"physics": 70,
                                                    "history": 80}}
              }
}
history = sampleDict.get("class")
print(sampleDict["class"]["student"]["marks"]["history"])

# Task3
# Создать программу, которая в зависимости от возраста того или
# иного человека из словаря votersDict решает кого допускать, а кого
# не допускать к голосованию.
votersDict = {'Denis': 32, 'Sergei': 21, 'Elena': 18, 'Timur': 17, 'Oleg': 27}
for i in votersDict.items():
        name = i[0]
        age = int(i[1])
        if age > 18:
                print(f"Вас зовут {name}, вам {age} и вы можете голосовать! ")
        else: print(f"Вас зовут {name}, вам {age} и вы НЕ  можете голосовать! ")
# Task4
# Ваша задача попросить ввести имя человека и в зависимости от его
# имени удалить от этого словаря. После удаления отобразите
# словарь, чтобы убедится что конкретный человек был удален из
# словаря
studentList = {'Oleg':"Moscow", 'Stepan': "Novosibirsk", 'Olga': "Ekaterenburg", "Murat":"Bishke", "David":"New Yourk"}
del studentList[input("Введите имя для удаления: ")]
print(studentList)