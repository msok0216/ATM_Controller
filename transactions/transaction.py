import uuid

'''
    The Transaction class acts as the parent class for Withdraw and Deposit
'''
class Transaction:
    def __init__(self, accountNumber):
        self.__id = uuid.uuid4()
        self.__accountNumber = accountNumber


    def getId(self):
        return self.__id
    
    def getAccountNumber(self):
        return self.__accountNumber
