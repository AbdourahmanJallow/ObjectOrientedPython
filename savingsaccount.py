from bankaccount import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, initial_balance=0, rate=0):
        super().__init__(initial_balance)
        self._rate = rate
        self._minBalance = initial_balance

    def setRate(self, rate):
        self._rate = rate

    def withdraw(self, amount):
        super().withdraw(amount)
        balance = self.getBalance()
        if balance < self._minBalance:
            self._minBalance = balance

    def monthEnd(self):
        interest = self._minBalance * (self._rate / 100)
        self.deposit(interest)
        self._minBalance = self.getBalance()

    # def getBalance(self):
    #     return self._minBalance
