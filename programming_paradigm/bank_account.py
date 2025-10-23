class BankAccount:
    """A class representing a bank account with basic operations."""
    
    def __init__(self, initial_balance=0):
        """Initialize a bank account with optional starting balance.
        
        Args:
            initial_balance (float, optional): Initial balance for the account. Defaults to 0.
        
        Raises:
            ValueError: If initial balance is negative
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            float: Updated account balance
            
        Raises:
            ValueError: If deposit amount is negative
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds exist.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False if insufficient funds
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display the current account balance in a formatted string.
        
        Returns:
            str: Formatted string showing current balance
        """
        return f"Current balance: ${self.account_balance:.2f}"