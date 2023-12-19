""" Необходимо создать следующие классы Vip_Account, PremiumAccount,
которые наследуются от класса BankAccount
1. В классе BankAccount есть методы
• deposit( ) – для пополнения денег – лимит в 10 000
• withdraw( ) – лимит для снятие денег в 10 000
• service( ) – При покупке или при вызове данного метода
происходит оплата за какой-нибудь сервис и предоставляется
скидка в 10%"""
class BankAccount():
    def __init__(self, account, replenish, deduce, service):
        self.__account = float(account)
        self.__replenish = replenish
        self.__deduce = deduce
        self.__service = service
    def get_balance(self):
        return print(f"{self.__account}$")
    def deposit(self, replenish):
        self.__replenish = replenish
        if self.__replenish > 10000:
            print("the deposit limit has been exceeded")
        else: self.__account = self.__account + self.__replenish
        print(f"Your balance now: {self.__account}$")
    def withdraw(self,deduce):
        self.__deduce = deduce
        if self.__deduce > 10000:
            print("deduce limit has been exceeded")
        else: self.__account = self.__account - self.__deduce
        print(f"Your balance now: {self.__account}$")
    def service(self,service):
        self.__service = service
        self.__account = self.__account - self.__service * 0.9
        print(f"Your balance now: {self.__account}$")
# vip = VipAccount(1000,100,200,200)
# vip.withdraw(50)
# premium = PremiumAccount(2000,None,None,None)
# premium.get_balance()
"""
2. В классе PremiumAccount необходимо переопределить методы в классе
родителе:
• deposit( ) – для пополнения денег – лимит в 50 000
• withdraw( ) – лимит для снятие денег в 50 000
• service( ) – При покупке или при вызове данного метода
происходит оплата за какой-нибудь сервис и предоставляется
скидка в 30%"""
class PremiumAccount(BankAccount):
    def deposit(self, replenish):
        if self.__replenish > 50000:
            print("the deposit limit has been exceeded")
        else: self.__account = self.__account + self.__replenish
        print(f"Your balance now: {self.__account}$")
    def withdraw(self,deduce):
        self.__deduce = deduce
        if self.__deduce > 50000:
            print("deduce limit has been exceeded")
        else: self.__account = self.__account - self.__deduce
        print(f"Your balance now: {self.__account}$")
    def service(self,service):
        self.__service = service
        self.__account = self.__account - self.__service * 0.7
        print(f"Your balance now: {self.__account}$")
"""3. В классе Vip_Account необходимо переопределить методы в классе
родителе:
• deposit( ) – для пополнения денег – лимит в 100 000
• withdraw( ) – лимит для снятие денег в 100 000
• service( ) – При покупке или при вызове данного метода
происходит оплата за какой-нибудь сервис и предоставляется скидка в 50%"""
class VipAccount(BankAccount):
    def __init__(self,account,replinish, deduce, service):
        super().__init__(account, replinish, deduce, service)
    def get_balance(self):
        return print(f"{self.__account}$")
    def deposit(self, replenish):
        self.__replenish = replenish
        if self.__replenish > 100000:
            print("the deposit limit has been exceeded")
        else: self.__account = self.__account + self.__replenish
        print(f"Your balance now: {self.__account}$")
    def withdraw(self,deduce):
        self.__deduce = deduce
        if self.__deduce > 100000:
            print("deduce limit has been exceeded")
        else: self.__account = self.__account - self.__deduce
        print(f"Your balance now: {self.__account}$")
    def service(self,service):
        self.__service = service
        self.__account = self.__account - self.__service * 0,5
        print(f"Your balance now: {self.__account}$")