class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance 
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
        elif amount > self.__balance :
            print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")
    
    def get_balance(self):
        return f"Current balance: {self.__balance}"


account = BankAccount(1000)
print(account.deposit(500))    
print(account.withdraw(200)) 
print(account.get_balance())  