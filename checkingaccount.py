from bankaccount import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)
        self._withdrawals = 0

    # charges $1.00 for every extra withdrawal in a month
    def withdraw(self, amount):
        FREE_WITHDRAWALS = 3
        WITHDRAWAL_FEE = 1

        super().withdraw(amount)
        self._withdrawals += 1

        if self._withdrawals > FREE_WITHDRAWALS:
            super().withdraw(WITHDRAWAL_FEE)

    def monthEnd(self):
        self._withdrawals = 0
