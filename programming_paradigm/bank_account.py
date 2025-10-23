class BankAccount:
    """A class representing a bank account with basic operations."""
    
    def __init__(self, account_balance):
        """Initialize a bank account with starting balance.
        
        Args:
            account_balance (float): Initial balance for the account
        
        Raises:
            ValueError: If initial balance is negative
        """
        if account_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_balance = account_balance

    def deposit(self, amount):
        '''Add the specified amount to the account balance'''
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        '''Subtract the specified amount from the account balance if sufficient funds exist'''
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.account_balance:
            raise ValueError("Insufficient funds for withdrawal")
        self.account_balance -= amount
        return self.account_balance
    
    def display_balance(self):
        '''Return the current account balance'''
        return f"Current balance: ${self.account_balance:.2f}"