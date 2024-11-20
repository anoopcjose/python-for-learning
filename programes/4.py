class bank_account:
    def __init__(self,balance):
        self.balance = balance

    def withdraw(self, withdrawal_amount):
        self.balance = self.balance - withdrawal_amount
        print(self.balance)
    def deposit(self,deposit_amount):
        self.balance = self.balance + deposit_amount
        print(self. balance)

deposit_bank_account = bank_account(2000)
deposit_bank_account.deposit(500)



