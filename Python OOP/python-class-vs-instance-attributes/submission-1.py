class BankAccount: 
    total_accounts = 0
    total_balance = 0  
    
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
    def update_accounts(self)-> None:
        BankAccount.total_accounts += 1

    def update_balance(self)-> None:
        BankAccount.total_balance += balance
        
# TODO: Create two accounts
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
print(f"Alice's balance: {alice.balance}")
print(f"Bob's balance: {bob.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: {BankAccount.total_balance}")