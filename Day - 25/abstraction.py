'''
#from abc import ABC, abstractionmethod

class BankAccount('ABC'):
    def checkbalance(self):
        print("You can checkout your balance")

    def viewhistory(self):
        print("You can your transactions")

    def userinfo(self):
        print("You can see your details")

    def transactions(self):
        print("You can transfer money through netbanking")

    @abstractionmethod
    def deposit(self):
        pass
    @abstractionmethod
    def withdraw(self):
        pass


class CurrentAccount(BankAccount):
    def deposit(self):
        print("YOu can deposit - CA")

    def withdraw(self):
        print("You can withdraw - CA")


class SavingAccount(BankAccount):
    def deposit(self):
        print("YOu can deposit - SA")

    def withdraw(self):
        print("You can withdraw - SA")

class FixeDeposit(BankAccount):
    def deposit(self):
        print("YOu can deposit - FD")

    def withdraw(self):
        print("You can withdraw - FD")


class ZeroBalanceAccount(BankAccount):
    def deposit(self):
        print("YOu can deposit - ZBA")

    def withdraw(self):
        print("You can withdraw - ZBA")


class SalaryAccount(BankAccount):
    def deposit(self):
        print("YOu can deposit - SAA")

    def withdraw(self):
        print("You can withdraw - SAA")

amathya = ZeroBalanceAccount()
amathya.deposit()
amathya.withdraw()
amathya.checkbalance()
amathya.viewhistory()
amathya.userinfo()
amathya.transactions()


ramakanth = SalaryAccount()
ramakanth.deposit()
ramakanth.withdraw()
ramakanth.checkbalance()
ramakanth.viewhistory()
ramakanth.userinfo()
ramakanth.transactions()
'''    
    
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("You can checkout your balance")

    def viewhistory(self):
        print("You can your transactions")

    def userinfo(self):
        print("You can see your details")

    def transactions(self):
        print("You can transfer money through netbanking")

    def deposit(self):
        pass

    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class CurrentAccount(BankAccount):
    def deposit(self):
        print("You can deposit - CA")
    def withdraw(self):
        print("You can withdraw - CA")

class SavingAccount(BankAccount):
    def deposit(self):
        print("You can deposit - SA")
    def withdraw(self):
        print("You can withdraw - SA")

class FixedAccount(BankAccount):
    def deposit(self):
        print("You can deposit - FD")
    def withdraw(self):
        print("You can withdraw - FD")
        
class SalaryAccount(BankAccount):
    def deposit(self):
        print("You can deposit - SAA")
    def withdraw(self):
        print("You can withdraw - SAA")

class ZeroBalanceAccount(BankAccount):
    def deposit(self):
        print("You can deposit - ZBA")
    def withdraw(self):
        print("You can withdraw - ZBA")


ramakanth = ZeroBalanceAccount()
ramakanth.deposit()
ramakanth.withdraw()
ramakanth.checkbalance()
ramakanth.viewhistory()
ramakanth.userinfo()
ramakanth.transactions()


amathya = SalaryAccount()
amathya.deposit()
amathya.withdraw()
amathya.checkbalance()
amathya.viewhistory()
amathya.userinfo()
amathya.transactions()
