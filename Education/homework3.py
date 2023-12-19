# Homework3
# Task 1
CityList = ['Moscow', 'Bishkek', 'NY', 'Tashkent',
            'Almaty', 'Talas', 'NY', 'Moscow']
# delete Bishkek, NY
item = "Bishkek"
item2 = 'NY'
item3 = 'NY'
if item in CityList:
    CityList.remove(item)
if item2 in CityList:
    CityList.remove(item2)
if item3 in CityList:
    CityList.remove(item3)
print(CityList)
print(len(CityList))
# add words
CityList.insert(3,"Tokyo")
CityList.insert(4,"LA")
print(CityList)
# clear
# CityList.clear()
# print(CityList)
# del
del CityList [0:7]
print(CityList)
# Task 2
List1 = [34,31,5,53,1,34,5]
avgList1 = sum(List1)/len(List1)
print(avgList1)
# Task 3
ListWorker = ['Elena','Gennady',
              'Evgeniia','Dmitry','Petr','Valentin']
print(ListWorker.remove(input("Введите имя для удаления:")))
print( f"Новый список после удаления:{ListWorker}")