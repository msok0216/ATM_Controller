"""
    Class for storing relevant card information
"""
class Card:
    def __init__(self, owner, accountNumber, expirationDate, cvv, cardNumber):
        self.__owner = owner
        self.__accountNumber = accountNumber
        self.__expirationDate = expirationDate
        self.__cvv = cvv
        self.__cardNumber = cardNumber
    

    def getOwner(self):
        return self.__owner
    def getAccountNumber(self):
        return self.__accountNumber
    def getExpirationDate(self):
        return self.__expirationDate
    def getCVV(self):
        return self.__cvv
    def getCardNumber(self):
        return self.__cardNumber
    