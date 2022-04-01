from transactions.transaction import Transaction

class Account:
    def __init__(self, owner, accountNumber, balance=0):
        self.__owner = owner
        self.__accountNumber = accountNumber
        self.__balance = balance
        self.__transactions = []
    
    def getAccountNumber(self):
        return self.__accountNumber

    def getBalance(self):
        return self.__balance
    
    def getOwner(self):
        return self.__owner

    def withdraw(self, amount):
        if self.getBalance() < amount:
            raise ValueError("Not Enough Balance")
        else:
            self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def getTransactions(self):
        return self.__transactions

    def addTransaction(self, transaction):
        self.getTransactions().append(transaction)

