class Employee():
    def __init__(self,e_id,name,salary):
        self.e_id=e_id
        self.name=name
        self.salary=salary
class DataEngineer(Employee):
    def __init__(self,e_id,name,salary,technology):
        super().__init__(e_id,name,salary)
        self.technology=technology
d1 = DataEngineer(101, "Rasik", 60000, "Python")
print(d1.name)
print(d1.e_id)
print(d1.salary)
print(d1.technology)