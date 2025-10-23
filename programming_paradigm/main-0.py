import sys
from bank_account import BankAccount

def main():
    # Create a BankAccount instance with an initial balance of 1000
    account = BankAccount(1000)
    
    print("Initial Balance:", account.display_balance())
    
    # Deposit 500
    try:
        new_balance = account.deposit(500)
        print("Balance after depositing 500:", new_balance)
    except ValueError as e:
        print("Error during deposit:", e)
    
    # Withdraw 200
    try:
        new_balance = account.withdraw(200)
        print("Balance after withdrawing 200:", new_balance)
    except ValueError as e:
        print("Error during withdrawal:", e)
    
    # Attempt to withdraw more than the balance
    try:
        new_balance = account.withdraw(2000)
        print("Balance after withdrawing 2000:", new_balance)
    except ValueError as e:
        print("Error during withdrawal:", e)

if __name__ == "__main__":
    main()
    