class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount, "| New Balance:", self.__balance)
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrew:", amount, "| New Balance:", self.__balance)
        else:
            print("Insufficient funds!")


# Test
account = BankAccount(1000)
account.deposit(500)
account.withdraw(2000)
account.withdraw(300)
print("Final Balance:", account.get_balance())
