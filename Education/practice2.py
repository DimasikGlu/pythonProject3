# Примите от пользователя данные
name = str(input('Введите имя:'))
age = input('Введите возраст:')
sex = input('Введите пол:')
Namecompany = input('Введите имя компании:')
maritalstatus = input('Введите семейное положение: ')
adress = input('Введите адрес проживания:')
# измерить длину имени
print(len(name))
# вторую букву в адресе
print(adress[2])
# проверить в названии компании "а"
print('a' in Namecompany)
# выведите имя со второй буквы и до конца
print(name[1:])
# обратные порядк наименование компании
print(Namecompany[::-1])
# 6. Строки
# .f формат
print(
    "Введите имя: {0} \nВведите возраст: {1} \nВведите пол: {2} \nВведите имя компании: {3} \nВведите семейное положение: {4}\nВведите адрес проживания: {5}".format(
        name, age, sex, Namecompany, maritalstatus, adress))
# .f-str
print(f"Введите имя: {name} \nВведите возраст: {age} \nВведите пол: {sex} "
      f"\nВведите имя компании: {Namecompany} \nВведите семейное положение: {maritalstatus}\nВведите адрес проживания: {adress}")

text = """ 
Белеет парус одинокой
В тумане моря голубом!..
Что ищет он в стране далекой?
Что кинул он в краю родном?..

Играют волны — ветер свищет,
И мачта гнется и скрыпит...
Увы! он счастия не ищет
И не от счастия бежит!
"""
print(text)

