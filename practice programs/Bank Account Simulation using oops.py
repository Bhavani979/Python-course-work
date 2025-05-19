class Bankaccount:
    def __init__(self,owner):
        self.owner=owner
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient Balance")
    def show_balance(self):
        print(f"Balance:{self.balance}")
acc=Bankaccount("Jannu")
acc.deposit(5000)
acc.withdraw(1000)
acc.show_balance()