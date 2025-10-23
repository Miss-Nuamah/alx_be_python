class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0


    def deposit(self,amount):
        '''Add the specified amount to the account balance'''
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self,amount):
        '''Subtract the specified amount from the account balance if sufficient funds exist'''
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.account_balance:
            raise ValueError("Insufficient funds for withdrawal")
        self.account_balance -= amount
        return self.account_balance
    
    def display_balance(self):
        '''Return the current account balance'''
        return self.account_balance

