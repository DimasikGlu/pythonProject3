"""
1. Создать класс BankAccount с приватными параметрами у которых есть
Set и Get методы:
• Id - Строковый тип данных
• balance - Тип данных Int или Float
Создать экземпляр этого класса и задать для него данные через
конструктор.
Дополнительно реализовать следующие методы:
• Deposit - Через этот метод человек восполняет баланс и баланс
увеличивается.
После депозита средств на счет должно выводится следующее
сообщение:
«Вы пополнили счет 123231434000034 на сумму: 25000 сом
Баланс после пополнения счета: 60000 сом»
• Withdraw - Снятие денег, через этот метод происходит снятие денег и
после снятия происходит снижение текущего баланса, в случае если
денег на балансе нету то, выводится сообщение:
«У вас закончились деньги на балансе»
Иначе
«Вы сняли со счета 123231434000034: 15000 сом
Баланс после пополнения счета: 35000 сом
Текущий баланс:35000 сом»
Пример результата выполнения программы:
Текущий баланс: 50000 сом
Вы сняли со счета 123231434000034: 15000 сом
Баланс после пополнения счета: 35000 сом
Текущий баланс:35000 сом
Вы пополнили счет 123231434000034 на сумму: 25000 сом
Баланс после пополнения счета: 60000 сом"""
class BankAccount():
    def __init__(self, Id, balance):
        self.__id = str(Id)
        self.__balance = float(balance)
    def get_info(self):
        print(f'Information about your deposit...\n'
              f'Id: {self.__id}\n'
              f'Balance: {self.__balance} USD')
    def Deposit(self,balance_up):
        self.__balance = self.__balance + balance_up
        print(f'You amount of deposits {self.__id}: {balance_up} USD\n'
              f'Current balance - {self.__balance} USD')
    def Withdraw(self,balance_down):
        self.__balance = self.__balance - balance_down
        if self.__balance <= 0:
            print('Ran out of money....')
            pass
        else: print(f'You withdrawn of deposits {self.__id}: {balance_down} USD\n'
              f'Current balance - {self.__balance} USD')
Gena = BankAccount(123000000, 5000)
Gena.Deposit(3000)
Gena.Withdraw(20000)
Gena.get_info()
