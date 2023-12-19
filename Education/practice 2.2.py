# practice2.2
FIO = input("ФИО:").upper()
print(FIO)
Surname, name, middlename = FIO[:9], FIO[10:17], FIO[-12:]

print(f"Name: {name}"
      f"\nMiddle name: {middlename}"
      f"\nSurname: {Surname}")
print(f"Количество символов в отчестве: {len(middlename)}")

# задание 2
cityname = str ("Bishkek")
new_cityname =cityname.rjust(8,' ')
new_cityname =new_cityname.rjust(9,'y')
new_cityname =new_cityname.rjust(10,'t')
new_cityname =new_cityname.rjust(11,'i')
new_cityname =new_cityname.rjust(12,'C')
print(new_cityname)
#Task 3
print (''.join(reversed(input("Введите текст: "))))
text = "I like living in Bishkek"
# lower
text2 = (text).lower()
print(f"{text2}")
# amount
print(text.count('i'))
print(text.count('k'))
# change words
print(text.replace('living in Bishkek','driving in Tokyo'))
# first ten words
print(text [0:10]) #первые 10 символов
print(text [0:12]) #первые 10 букв
# bring words
text3 = text[2:13]
print(f"{text3}")