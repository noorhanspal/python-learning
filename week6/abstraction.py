from abc import ABC, abstractmethod

# Abstract Class
class Bank(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# SBI Bank class inheriting Bank
class SBI(Bank):
    def deposit(self, amount):
        print("Deposited", amount, "in SBI account")

    def withdraw(self, amount):
        print("Withdrew", amount, "from SBI account")


# PNB Bank class inheriting Bank
class PNB(Bank):
    def deposit(self, amount):
        print("Deposited", amount, "in PNB account")

    def withdraw(self, amount):
        print("Withdrew", amount, "from PNB account")


# Object Creation
sbi_acc = SBI()
pnb_acc = PNB()
sbi_acc.deposit(5000)     
sbi_acc.withdraw(2000)    
pnb_acc.deposit(7000)     
pnb_acc.withdraw(3000)     