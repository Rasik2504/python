# Create an abstract class Shape with an abstract method area().
# Create Circle, Rectangle, and Triangle classes.
# Each class should calculate its own area.
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self,lenght,breath):
        self.length=lenght
        self.breath=breath
    def area(self):
        return self.length * self.breath
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
c1=Circle(4)
r1=Rectangle(10,10)
t1=Triangle(2,8)
areas=[c1,r1,t1]
for i in areas:
    print(i.area())
