class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
    def display(self):
        print("Area of Rectangle is : ",self.area())
res=Rectangle(4,5)
res.display()