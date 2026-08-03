class Rectangle:
    def __init__(self,ln,wd):
        self.ln=ln
        self.wd=wd
    def area(self):
        return self.ln * self.wd
    def display(self):
        print("Area : ",self.area())
cal=Rectangle(10,20)
cal.display()