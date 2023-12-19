# 1 Принять текст и отобразить в обратном порядке
text = input("Введите текст: ")
print(text[::-1])
# 2 Работа с текстом
text2 = 'Я обучаюсь курсу Python Django'
print('Название курса:', text2[-13:])
# 3 Убрать лишние символы
text3 = '$$$Python@@@'
text4 = '%%%Programming'
text5 = 'City&&&'
text6 = '****Computer***'
print(text3.strip('$@'))
print(text4.lstrip("%"))
print(text5.rstrip('&'))
print(text6.strip('*'))
# 4 Задание
favnumber = str(input("Любимое число: "))
favcolor = str(input("Любимый цвет: "))
favcity = str(input("Любимый город: "))
favfood = str(input("Любимая еда: "))
print('Любимое число: {0} \nЛюбимый цвет: {1} \nЛюбимый гороl: {2}\nЛюбимая еда: {3}'.format(favnumber, favcolor,favcity, favfood))
print(f"Любимое число: {favnumber} \nЛюбимый цвет: {favcolor} \nЛюбимый город: {favcity} "
      f"\nЛюбимая еда: {favfood}")
