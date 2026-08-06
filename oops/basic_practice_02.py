# Create a Laptop class
# Attributes:
# - brand
# - RAM
# - processor
# - price
#
# Create 3 laptop objects.
class laptop:
    def __init__(self,brand,ram,processor,price):
        self.brand=brand
        self.ram=ram
        self.processor=processor
        self.price=price
    def display(self):
        print("Brand",self.brand)
        print("RAM",self.ram)
        print("Processor",self.processor)
        print("Price",self.price)
l1=laptop("HP","8GB","M3",40000)
l2=laptop("Apple","32GB","M3",90000)   
l1.display()
l2.display()    

          