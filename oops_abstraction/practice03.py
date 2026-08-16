from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print("Pay Through UPI")
    def refund(self,amount):
        print("Refund through UPI")
class CreditCard(Payment):
    def pay(self,amount):
        print("Pay Through CreditCard")
    def refund(self,amount):
        print("Refund through Creditcard")
class NetBanking(Payment):
    def pay(self,amount):
        print("Pay Through Netbanking")
    def refund(self,amount):
        print("Refund through Netbanking")
upi=UPI()
creditcard=CreditCard()
netbanking=NetBanking()
upi.pay(500)
creditcard.pay(200)