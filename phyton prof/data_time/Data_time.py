# Task1
"""При помощи атрибутов day month year выведите дату, хранящуюся в
переменной user_date , в формате день.месяц.год
На день и месяц нужно обязательно отвести 2 знака под вывод, на год - четыре
знак"""
from datetime import *
user_date = datetime(2025,2,12)
print(user_date.strftime("%d-%m-%Y"))

# Task2
"""2.Необходимо выяснить дату от сегодняшнего дня через неделю и 2 часа?"""
now = datetime.now()
time_delta = timedelta(days=7,hours=2)
print(now+time_delta)

# Task3
"""3.Выясните какая дата была 10 дней назад от сегодняшней даты?"""
now = datetime.now()
time_delta = timedelta(days=10)
print(now-time_delta)