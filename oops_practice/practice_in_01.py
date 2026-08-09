class Vehicle:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def display(self):
        print(" moving",self.start)
        print("mpving : ",self.end)
c1=Vehicle("f","e")
class Car(Vehicle):
    def __init__(self,model):
        self.model=model
    def display(self):
        print("go",self.model)
c2=Car("kia")
c2.display()
c1.display()