import uuid
from card import Card
from account import Account
from transactions.withdraw import Withdraw
from transactions.deposit import Deposit

'''
The ATM object communicates with bank to confirm card and receive necessary account information
'''
class ATM:

  def __init__(self):
    self.__id = uuid.uuid4()
    self.__account = None
    self.__card = None
    self.__transactions = []
    self.__balance = 1000000
    # can also add other fields from hardware such as cash balance of atm

  def getId(self):
    return self.__id
  
  def getTransactions(self):
    return self.__transactions
  
  def getCurrAccount(self):
    return self.__account
  
  # returns the cash balance for the ATM
  def getATMBalance(self):
    return self.__balance

  def getCard(self):
    return self.__card

  def setCard(self, card):
    self.__card = card
  
  def setAccount(self, account):
    self.__account = account

  # If a card is inserted, validate the card
  # If the card isn't valid, exit the process and eject the card
  def insertCard(self, card, pin):
    if not self.validate(card, pin):
      self.__exit()
      self.ejectCard()
      return False
    self.setCard(card)
    self.setAccount(Account(card.getOwner(), card.getAccountNumber()))
    return True

  def ejectCard(self):
    pass

  # Communicate with bank to confirm card info
  # Confirm pin and if the pin is valid, set current account to the object retrieved from the bank
  def validate(self, card, pin):
    try:
      if self.__confirmPIN(card, pin):
        return True
      else:
        raise ValueError('Invalid Card')

    except ValueError as e:
      print(str(e))
      return False
    
  def __confirmPIN(self, card, pin):
    return True


  def initiateTransaction(self, action, amount=0):
    try:
      if action == "Check":
        return self.__checkAccountBalance()
      else:
        if amount < 0: 
          raise ValueError("Invalid Input for Transaction Amount")
        elif action == "Withdraw":
          self.__withdraw(amount)
          t = Withdraw(self.getCurrAccount().getAccountNumber(), amount)
          self.__balance -= amount
          self.__transactions.append(t)
          self.getCurrAccount().addTransaction(t)
          return self.getCurrAccount().getBalance()
        elif action == "Deposit":
          self.__deposit(amount)
          t = Deposit(self.getCurrAccount().getAccountNumber(), amount)
          self.__balance += amount
          self.__transactions.append(t)
          self.getCurrAccount().addTransaction(t)
          return self.getCurrAccount().getBalance()

    except (ValueError, TypeError) as e:
      print(str(e))
      self.__exit()
      self.ejectCard()
      return False

  def __deposit(self, amount):
    self.getCurrAccount().deposit(amount)
    self.__balance += amount
    return self.getCurrAccount().getBalance()
    # Add amount to cash bin balance in the future

  def __withdraw(self, amount):
    self.getCurrAccount().withdraw(amount)
    self.__balance -= amount
    return self.getCurrAccount().getBalance()
    # Subtract amount from cash bin balance in the future

  # returns 
  def __checkAccountBalance(self):
    return self.getCurrAccount().getBalance()

  def __exit(self):
    self.__account = None
    self.__card = None
  

