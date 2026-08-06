class Bank:
    Bank="ICICI"
    IFSC_code=12201
    def __init__(self,acc_num,cust_name,email,bal):
        self.acc_num=acc_num
        self.cust_name=cust_name
        self.email=email
        self.bal=bal

    @classmethod
    def change_ifsc(cls,new_ifsc):
        cls.IFSC_code=new_ifsc

    def display(self):
        print("Bank :", Bank.Bank)
        print("IFSC Code :", Bank.IFSC_code)
        print("Account Number :", self.acc_num)
        print("Customer Name :", self.cust_name)
        print("Balance :", self.bal)
        print("Email :", self.email)


    def deposit(self,money):
        self.bal+=money

    def withdraw(self,money):
        if money<=self.bal:
            self.bal-=money
        else:
            print("Insufficient Balance")

    def check(self):
        print("Balance",self.bal)
    
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

customer1=Bank(101,"Rosy","rosy@gmail.com",120000)
customer1.display()
customer1.change_ifsc(1288)
print("\n")
customer1.display()
customer1.deposit(100)
customer1.check()
customer1.withdraw(800)
customer1.check()