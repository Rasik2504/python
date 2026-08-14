# QUESTION 3: BANK ACCOUNT
#
# Create a class called BankAccount.
#
# Requirements:
# 1. The class should contain:
#    - account_holder
#    - private variable __balance
#
# 2. Use __init__() to initialize the account holder
#    and starting balance.
#
# 3. Create a method deposit(amount)
#    that adds money to the balance.
#
# 4. Create a method withdraw(amount)
#    that removes money from the balance.
#
# 5. The withdrawal should be allowed only if:
#       amount <= balance
#
# 6. If the user tries to withdraw more money
#    than the available balance, print:
#       "Insufficient balance"
#
# 7. Create a method get_balance()
#    that returns the current balance.
#
# 8. Create one BankAccount object.
#
# 9. Deposit some money.
#
# 10. Withdraw some money.
#
# 11. Try withdrawing more money than the balance.
#
# Concepts to practice:
# - Encapsulation
# - Private variable
# - Methods
# - Object state
# - Conditional statements inside methods
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def display(self):
        print("Acoount Holder : ",self.account_holder)
        print("Balance : ",self.get_balance())
    def deposit(self,amount):
        if(amount>0):
            self.__balance=self.__balance+amount
        else:
            print("Invalid Amount")
    def withdraw(self,amount):
        if(amount>0):
            self.__balance=self.__balance-amount
        else:
            print("Invalid Amount")
c1=BankAccount("Alice",2000)
c1.display()
c1.deposit(2000)
c1.display()
c1.withdraw(500)
c1.display()