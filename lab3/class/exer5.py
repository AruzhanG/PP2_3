class Account:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(name + ", you entered",amount,"in your bank account")
        else:
            print("unvailable!")    
    
    def withdraw(self,amount):
        if amount > 0:
            if amount < self.balance:
                self.balance = amount
                print(name+",you withdraw", amount,"money drom your deposit")
            else:
                print(name+"You cannot withdraw this amount of money right now")
        else:
            print(name + "You should take more money than 0")
            
            
name = input()
"""amount = int(input())"""
account = Account(name)

account.deposit(500)
account.withdraw(300)
account.withdraw(3000)
account.withdraw(0)

print(name + "You have:", account.balance)
            