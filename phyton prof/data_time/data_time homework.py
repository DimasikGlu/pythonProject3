from datetime import *

import sshuttle as sshuttle

"""Task1. Примите от пользователя дату в следующем формате
d-m/yyy-(H:M:S)
Создайте на основе принятого от пользователя времени новую дату"""
def Task1(date_user):
    from datetime import datetime
    date1 = datetime.strptime(date_user,'%d-%m/%Y-(%H:%M:%S)')
    return date1


"""2. Созданную дату из задания No1 переделайте в следующий формате
«день-название месяца полностью-(день недели)-год с двумя цифрами -
Часы:
Минута»
Пример: 23-August - Wed - 22 - 6:30"""
def Task2(date1):
    print(date1.strftime("%d-%b-%A-%y-%H-%M"))

# """3. Выясните какое будет время спустя:
# • 2 месяца от текущей даты?
# • через 2 Года?
# • Через год и 2 дня?
# • Через 3 месяца и 3 дня?
# И отобразите эти значения на экране"""
def Task3(now):
    timedelta1 = timedelta(days=60)
    print(now+timedelta1)
    timedelta2 = timedelta(days=365*2)
    print(now+timedelta2)
    print(now+timedelta(days=367))
    print(now+timedelta(days=93))



if __name__ == '__main__':
    date_user = input('input data (d-m/yyyy-(H:M:S): ')
    Task1(date_user)

    date2 = Task1(date_user)
    Task2(date2)

    now = datetime.now()
    Task3(now)
