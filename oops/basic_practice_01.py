class Employee:
    def __init__(self,employee_id,name,salary):
        self.employee_id=employee_id
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee ID : ",self.employee_id)
        print("Name : ",self.name)
        print("Salary : ",self.salary)
emp1=Employee(1,"Rasik",10000)
emp2=Employee(2,"Rahman",20000)
emp3=Employee(2,"Hassan",30000)
emp1.display()
emp2.display()
emp3.display()
