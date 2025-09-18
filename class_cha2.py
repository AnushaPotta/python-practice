class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def display(self):
        print(f"Name: {self.owner}, balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"New balance after deposit: {self.balance}")

    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance = self.balance - amount
            print(f"New balance after withdrawl is {self.balance}")
        else:
            print("Not enough balance")
    def transfer(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print(f"{amount} tranferred from {self.owner} to {other_account.owner}")
            print(f"{self.owner}'s balance is {self.balance}")
            print(f"{other_account.owner}'s balance is {other_account.balance}")
        else:
            print(f"{self.owner} has insufficent balance")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"New balance after adding interest: {self.balance}")
            


acc1 = BankAccount("Pal", 1000)
acc2 = BankAccount("Jhon", 2000)

acc1.display()
acc2.display()

acc1.deposit(100)
acc2.deposit(100)

acc1.withdraw(100)
acc2.withdraw(100)

acc1.withdraw(1001)

acc1.transfer(acc2, 100)

acc1 = SavingsAccount("Pam", 3000, 0.1)
acc1.display()
acc1.add_interest()



    

