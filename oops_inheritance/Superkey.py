class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
s1=Person("Rasik",19)
print(s1.name)
print(s1.age)
