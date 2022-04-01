import uuid
class Transaction:
    def __init__(self, accountNumber):
        self.__id = uuid.uuid4()
        self.__accountNumber = accountNumber


    def getId(self):
        return self.__id
    
    def getAccountNumber(self):
        return self.__accountNumber
