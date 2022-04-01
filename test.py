import unittest
from account import Account
from card import Card
from atm import ATM
from datetime import date
from transactions.deposit import Deposit
from transactions.withdraw import Withdraw


class Test(unittest.TestCase):
    def setUp(self):
        self.w = Withdraw(456)
        self.d = Deposit(789)
        self.account = Account("Bear Robotics", '123456', 10000)
        self.card = Card("Bear Robotics", '123456', date(2030, 12, 31), '372', '6600332120098831')
        self.atm = ATM()

    def testWithdraw(self):
        self.assertEqual(self.w.getAccountNumber(), 456)
        self.w.setAmount(10000)
        self.assertEqual(self.w.getAmount(),10000)

    def testDeposit(self):
        self.assertEqual(self.d.getAccountNumber(), 789)
        self.d.setAmount(10000)
        self.assertEqual(self.d.getAmount(), 10000)

    def testCard(self):
        self.assertEqual(self.card.getAccountNumber(), '123456')
        self.assertEqual(self.card.getOwner(), "Bear Robotics")
        self.assertEqual(self.card.getExpirationDate(), date(2030, 12, 31))
        self.assertEqual(self.card.getCVV(), '372')
        self.assertEqual(self.card.getCardNumber(), '6600332120098831')
    
    def testAccount(self):
        self.assertEqual(self.account.getAccountNumber(), '123456')
        self.assertEqual(self.account.getBalance(), 10000)
        self.assertEqual(self.account.getOwner(), "Bear Robotics")

        self.account.withdraw(10000)
        self.assertEqual(self.account.getBalance(), 0)

        self.account.deposit(100000)
        self.assertEqual(self.account.getBalance(), 100000)

    def testATM(self):
        self.assertIsNotNone(self.atm)
        self.assertEqual(self.atm.getATMBalance(), 1000000)
        
        self.assertTrue(self.atm.validate(self.card, 1121))
        self.assertTrue(self.atm.insertCard(self.card, 1121))

        self.atm.setAccount(self.account)
        self.assertEqual(self.account, self.atm.getCurrAccount())

        self.assertEqual(self.atm.initiateTransaction("Withdraw", 10000), 0)
        self.assertTrue(isinstance(self.atm.getTransactions()[-1], Withdraw))
        self.assertEqual(self.atm.getTransactions()[0].getAmount(), 10000)
        self.assertEqual(self.atm.getCurrAccount().getTransactions()[-1].getAmount(), 10000)
        self.assertFalse(self.atm.initiateTransaction("Withdraw", -10000))

        self.atm.setAccount(self.account)

        self.assertEqual(self.atm.initiateTransaction("Deposit", 90000), 90000)
        self.assertTrue(isinstance(self.atm.getTransactions()[-1], Deposit))
        self.assertEqual(self.atm.getTransactions()[-1].getAmount(), 90000)
        self.assertEqual(self.atm.getCurrAccount().getTransactions()[-1].getAmount(), 90000)
        self.assertFalse(self.atm.initiateTransaction("Deposit", -10000))

        self.assertIsNone(self.atm.getCurrAccount())
        self.assertIsNone(self.atm.getCard())



if __name__ == '__main__':
    unittest.main()