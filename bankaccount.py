class BankAccount:

    def __init__(self, initial_balance=0.0):
        self._balance = initial_balance

    # def setBalance(self, balance):
    #     self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    # month end, performs operation after month ends
    def monthEnd(self):
        return

    def getBalance(self):
        return self._balance
