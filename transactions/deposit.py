from transactions.transaction import Transaction

'''
    Class for Desposit Transactions
'''
class Deposit(Transaction):
    def __init__(self, accountNumber, amount=0):
        super().__init__(accountNumber)
        self.__amount = amount

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount):
        self.__amount = amount