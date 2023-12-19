# import calendar
# import datetime
# import pytz
#
# # Task1
# """Примите от пользователя год и число месяца и в зависимости от
# этого составьте календарь."""
# # data = calendar.TextCalendar(calendar.TUESDAY)
# # user_year = int(input('please input year - '))
# # user_month = int(input('please input month - '))
# # data_calen = data.formatmonth(user_year,user_month)
# # print(data_calen)
# # Task2
# """Сгенерируйте список дней принятое от пользователя в задании No1,
# где в качестве дня недели установлен Вторник"""
# # list1 = []
# # for i in data_calen.iterweekdays():
# #     if i != 0:
# #         list1.append(i)
# # print(list1)
# # for data_calen in calendar.day_name:
# #     print(data_calen)
#
# # for i in range(1,13):
# #     month = calendar.monthcalendar(user_year,user_year)
# #     print(month)
# # # Task3
# """Сгенерируйте HTML код принятое от пользователя в задании No1,
# где в качестве дня недели установлен Вторник"""
# # d_html = calendar.HTMLCalendar(calendar.TUESDAY)
# # data_html = d_html.formatmonth(2022, 12)
# # print(data_html)
#
# # Task4
# # Примите от пользователя любую дату и время и сконвертируйте эту
# # дату и время для следующих временных зон (можно любой город
# # взять из этих стран):
# # • Франция
# # • Япония
# # • Австралия
# # • Южная Африка
# # • Индия
#
#
# # Task5
# import locale
# print(f'1.France\n2.Japan\n3.Australia\n4.South Africa\n5.India\n')
# def Task5 (choice_user):
#     choise_user = ()
#     if choice_user == '1':
#         local_France = datetime.datetime.now(pytz.timezone('Europe/Paris'))
#         print(local_France)
#     elif choice_user == '2':
#         local_Japan = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
#         print(local_Japan)
#     elif choice_user == '3':
#         local_Australia = datetime.datetime.now(pytz.timezone('Australia/Sydney'))
#         print(local_Australia)
#     elif choice_user == '4':
#         local_Africa = datetime.datetime.now(pytz.timezone('Africa/Johannesburg'))
#         print(local_Africa)
#     elif choice_user == '5':
#         local_India = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
#         print(local_India)
#     else: print('Your choise uncorrect')
#
# if __name__ == '__main__':
#     Task5(choice_user=input(('Input number:')))
#
#
