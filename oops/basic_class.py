class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
s1=Student("Rasik",20)
s2=Student("Rahman",21)
s1.display()
s2.display()