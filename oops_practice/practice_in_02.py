#single inheritance
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₹{amount}")

    def show_balance(self):
        print(f"Balance: ₹{self.balance}")


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        interest = self.balance * 0.04
        print(f"Interest: ₹{interest}")


account = SavingsAccount("Anisha", 50000)

account.deposit(5000)
account.show_balance()
account.calculate_interest()

#Multilevel Inheritance
class Order:

    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    def show_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Amount: ₹{self.amount}")


class OnlineOrder(Order):

    def __init__(self, order_id, amount, address):
        super().__init__(order_id, amount)
        self.address = address

    def show_delivery_address(self):
        print(f"Delivery Address: {self.address}")


class InternationalOrder(OnlineOrder):

    def __init__(self, order_id, amount, address, customs_charge):
        super().__init__(order_id, amount, address)
        self.customs_charge = customs_charge

    def show_customs_charge(self):
        print(f"Customs Charge: ₹{self.customs_charge}")


order = InternationalOrder("101",50000,"Chennai",5000)

order.show_order()
order.show_delivery_address()
order.show_customs_charge()

#Multiple Inheritance
class Developer:

    def write_code(self):
        print("Writing production code")

    def review_code(self):
        print("Reviewing code")


class Manager:

    def manage_team(self):
        print("Managing development team")

    def conduct_meeting(self):
        print("Conducting team meeting")


class TechnicalLead(Developer, Manager):

    def lead_project(self):
        print("Leading technical project")


lead = TechnicalLead()

lead.write_code()
lead.review_code()
lead.manage_team()
lead.conduct_meeting()
lead.lead_project()

#Hierarchical Inheritance
class Employee:

    def __init__(self, name):
        self.name = name

    def login(self):
        print(f"{self.name} logged in")


class Developer(Employee):

    def write_code(self):
        print("Writing application code")


class Manager(Employee):

    def manage_team(self):
        print("Managing team")


class TechnicalLead(Developer):

    def lead_developers(self):
        print("Leading development team")


developer = Developer("Rahul")
manager = Manager("Priya")
lead = TechnicalLead("Arun")

developer.login()
developer.write_code()

manager.login()
manager.manage_team()

lead.login()
lead.write_code()
lead.lead_developers()

#hybrid
class Employee:

    def __init__(self, name):
        self.name = name

    def login(self):
        print(f"{self.name} logged in")


class Developer(Employee):

    def write_code(self):
        print("Writing application code")


class Manager(Employee):

    def manage_team(self):
        print("Managing team")


class TechnicalLead(Developer):

    def lead_developers(self):
        print("Leading development team")


developer = Developer("Rahul")
manager = Manager("Priya")
lead = TechnicalLead("Arun")

developer.login()
developer.write_code()

manager.login()
manager.manage_team()

lead.login()
lead.write_code()
lead.lead_developers()