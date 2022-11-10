from bankaccount import BankAccount
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

# accounts = [
#     SavingsAccount(1000, 5),
#     SavingsAccount(4500, 7.5),
#     SavingsAccount(28_000, 9)
# ]
accounts = [
    CheckingAccount(80_000),
    CheckingAccount(32_500),
    CheckingAccount(18_000)
]
done = False
while not done:
    print("D)eposit W)ithdraw M)onth end Q)uit")
    response = input("> ")
    if response.upper() == "D" or response.upper() == "W":
        # account number is associated with the
        # position of the account in the list
        print("Enter account number and amount: ")
        accountNumber = int(input("> "))
        amount = float(input("> "))

        if response.upper() == "D":
            accounts[accountNumber].deposit(amount)
        else:
            accounts[accountNumber].withdraw(amount)
        print("Balance: $", accounts[accountNumber].getBalance())

    elif response.upper() == "M":
        for i in range(len(accounts)):
            accounts[i].monthEnd()
            print(f"Account {(i+1)}: $", accounts[i].getBalance())

    elif response.upper() == "Q":
        done = True
