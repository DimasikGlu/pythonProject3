import pandas
import pandas as pd

"""1. Ваша задача принять от работников информации по следующим
полям:
• Имя
• Возраст
• Заработную плату
• Должность"""
def Task1():
    num_people = int(input('How many people: '))
    # name, age, salary, position = [],[],[],[]
    title = ["name","age","salary","position"]
    people_dict = {}
    i = 0
    for i in range(1,num_people):
        name = f'{input(f"Please input Name {i}:")}'
        age = f'{input(f"Please input age {i}:")}'
        salary = f'{input(f"Please input salary {i}:")}'
        position = f'{input(f"Please input position {i}:")}'
        people_dict = {'name':name , 'age':age ,'salary':salary , 'position':position}
        # people_dict_to_xlsx = pd.DataFrame(people_dict)
    print(people_dict)

# def Task2():

if __name__=='__main__':
    Task1()