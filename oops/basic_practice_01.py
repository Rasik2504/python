class Employee:
    def __init__(self,employee_id,name,salary):
        self.employee_id=employee_id
        self.name=name
        self.salary=salary
    def display(self):
        print("ID : ",self.employee_id)
        print("Name : ",self.name)
        print("Salary : ",self.salary)
emp1=Employee(1,"Anisha",100000)
emp2=Employee(2,"Rasik",2000)
emp1.display()
emp2.display()